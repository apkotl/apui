from typing import Annotated
from fastapi import APIRouter, Body, Query, HTTPException
from fastapi.responses import RedirectResponse

import jwt
import aiohttp

from src.core.exceptions import APIException
from src.shemas.auth import GoogleUriTestResponse
from src.config import settings
from src.config.google_oauth import generate_google_oauth_redirect_uri

from src.state_storage import state_storage

router = APIRouter(prefix="/auth", tags=["Auth"])

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
    return GoogleUriTestResponse(data=uri)


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
