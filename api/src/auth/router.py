
from typing import Annotated
from fastapi import APIRouter, Body, Query, HTTPException, Depends, status
from fastapi.responses import RedirectResponse

import jwt
import aiohttp

from src.core.schemas import ResponseSchema
from src.core.exceptions import APIException
from src.config import settings

from .config import generate_google_oauth_redirect_uri

from src.state_storage import state_storage
from .. import databases

router = APIRouter(prefix="/auth", tags=["Auth"])

#################################################
# Google
#################################################

@router.get("/google/uri", include_in_schema=False)
def get_google_auth_redirect_uri(
        mode: str | None = Query(None),
):
    func = settings.frontend_url
    if mode == "prod":
        func = settings.web_url
    uri = generate_google_oauth_redirect_uri(func)
    return RedirectResponse(url=uri, status_code=302)


@router.get("/google/uri/test")
def get_google_auth_redirect_uri_test(
        mode: str | None = Query(None),
):
    func = settings.frontend_url
    if mode == "prod":
        func = settings.web_url
    uri = generate_google_oauth_redirect_uri(func)
    return ResponseSchema[str](data=uri)


@router.post("/google/callback")
async def handle_code(
        code: Annotated[str, Body(embed=True)],
        state: Annotated[str, Body(embed=True)],
        mode: str | None = Query(None),
):
    if state not in state_storage:
        raise APIException(
            status_code=400,
            type="google_auth",
            detail="Google State incorrect!",
        )
    else:
        print("State correct")


    google_token_url = "https://oauth2.googleapis.com/token"
    func = settings.frontend_url
    if mode == "prod":
        func = settings.web_url

    async with aiohttp.ClientSession() as session:
        async with session.post(
            url=google_token_url,
            data={
                'client_id': settings.OAUTH_GOOGLE_CLIENT_ID,
                'client_secret': settings.OAUTH_GOOGLE_CLIENT_SECRET,
                'grant_type': "authorization_code",
                'redirect_uri': func(path='/auth/google'),
                'code': code,
            },
            ssl=False, # for dev only
        ) as response:
            res = await response.json()
            print(f"{res=}")

            try:
                id_token = res["id_token"]
                user_data = jwt.decode(
                    id_token,
                    algorithms=["RS256"],
                    options={"verify_signature": False},
                )
            except Exception as exp:
                raise HTTPException(
                    status_code=400,
                    detail={res}
                )


    print(f"{user_data=}")
    return {
        "user": user_data
    }


#################################################
# Auth JWT token
#################################################
import hashlib
from datetime import datetime, timezone

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.databases.dependencies import get_async_session

from .schemas import TokenResponse, LoginRequest, RefreshRequest
from .models import UsersOrm, RefreshTokensOrm

from .utils import jwt as jwt_utils





@router.post("/login", response_model=ResponseSchema[TokenResponse])
async def login(data: LoginRequest, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(UsersOrm).where(UsersOrm.email == data.email, UsersOrm.is_active == True)
        result = await session.execute(query)
        user: UsersOrm | None = result.scalars().first()

        if not user or not jwt_utils.verify_password(data.password, user.password_hash):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

        # Генерация токенов
        access_token = jwt_utils.create_access_token({"sub": str(user.id), "email": user.email})
        refresh_token, refresh_exp = jwt_utils.create_refresh_token({"sub": str(user.id)})

        # Убираем timezone информацию
        refresh_exp = refresh_exp.replace(tzinfo=None)

        # Сохраняем refresh в БД
        session.add(RefreshTokensOrm(
            user_id=user.id,
            token_hash=jwt_utils.hash_token(refresh_token),
            expires_at=refresh_exp
        ))
        await session.commit()

        #return TokenResponse(access_token=access_token, refresh_token=refresh_token)
        return ResponseSchema[TokenResponse](
            data = TokenResponse(access_token=access_token, refresh_token=refresh_token)
        )
    except HTTPException as e:
        raise
    except Exception as e:
        #logger.error(f"[{request_id}] Error getting book {book_id}: {str(e)}", exc_info=True)
        raise APIException(
            detail=str(e)
        )


@router.post("/refresh", response_model=TokenResponse)
async def refresh(data: RefreshRequest, session: AsyncSession = Depends(get_async_session)):
    try:
        payload = jwt_utils.decode_token(data.refresh_token)
        user_id = int(payload.get("sub"))
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

    try:
        # Проверяем, есть ли этот токен в БД и он не истёк
        token_hash = jwt_utils.hash_token(data.refresh_token)
        query = select(RefreshTokensOrm).where(
            RefreshTokensOrm.token_hash == token_hash,
            RefreshTokensOrm.user_id == user_id,
            RefreshTokensOrm.expires_at > datetime.now(timezone.utc).replace(tzinfo=None)
        )
        result = await session.execute(query)
        db_token = result.scalars().first()

        if not db_token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token expired or revoked")

        # Создаём новый access token
        access_token = jwt_utils.create_access_token({"sub": str(user_id)})
        refresh_token, refresh_exp = jwt_utils.create_refresh_token({"sub": str(user_id)})

        # Убираем timezone информацию
        refresh_exp = refresh_exp.replace(tzinfo=None)

        # Заменяем refresh токен в БД
        await session.delete(db_token)
        session.add(RefreshTokensOrm(
            user_id=user_id,
            token_hash=jwt_utils.hash_token(refresh_token),
            expires_at=refresh_exp
        ))
        await session.commit()

        return TokenResponse(access_token=access_token, refresh_token=refresh_token)
    except HTTPException as e:
        raise
    except Exception as e:
        #logger.error(f"[{request_id}] Error getting book {book_id}: {str(e)}", exc_info=True)
        raise APIException(
            detail=str(e)
        )


@router.post("/logout")
async def logout(data: RefreshRequest, session: AsyncSession = Depends(get_async_session)):
    token_hash = jwt_utils.hash_token(data.refresh_token)
    await session.execute(delete(RefreshTokensOrm).where(RefreshTokensOrm.token_hash == token_hash))
    await session.commit()
    return {"detail": "Logged out"}

"""
In Other Routers
from fastapi import Depends
from auth.dependencies import get_current_user
from src.models import UsersOrm

@router.get("/me")
async def get_me(current_user: UsersOrm = Depends(get_current_user)):
    return {"id": current_user.id, "email": current_user.email, "roles": [r.name for r in current_user.roles]}
"""
from src.auth.dependencies import get_current_user
@router.get("/me")
async def get_me(current_user: dict = Depends(get_current_user)):
    try:
        #return {"id": current_user.id, "email": current_user.email, "roles": [r.name for r in current_user.roles]}
        return ResponseSchema[dict](
            data={'sub': current_user.get('sub'), 'email': current_user.get('email')}
        )
    except HTTPException as e:
        raise
    except Exception as e:
        #logger.error(f"[{request_id}] Error getting book {book_id}: {str(e)}", exc_info=True)
        raise APIException(
            detail=str(e)
        )