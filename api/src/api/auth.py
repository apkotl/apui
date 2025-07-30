from typing import Annotated
from fastapi import APIRouter, Body
from fastapi.responses import RedirectResponse

import aiohttp

from src.shemas.auth import GoogleUriTestResponse
from src.config import settings
from src.config.google_oauth import generate_google_oauth_redirect_uri

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.get("/google/uri", include_in_schema=False)
def get_google_auth_redirect_uri():
    uri = generate_google_oauth_redirect_uri()
    return RedirectResponse(url=uri, status_code=302)


@router.get("/google/uri/test")
def get_google_auth_redirect_uri_test():
    uri = generate_google_oauth_redirect_uri()
    return GoogleUriTestResponse(data=uri)


@router.post("/google/callback")
async def handle_code(
        code: Annotated[str, Body(embed=True)],
):
    google_token_url = "https://oauth2.googleapis.com/token"
    port = "" if settings.IS_CONTAINER else ":5173"
    redirect_url = f"http://localhost{port}/auth/google"

    async with aiohttp.ClientSession() as session:
        async with session.post(
            url=google_token_url,
            data={
                'client_id': settings.OAUTH_GOOGLE_CLIENT_ID,
                'client_secret': settings.OAUTH_GOOGLE_CLIENT_SECRET,
                'grant_type': "authorization_code",
                'redirect_uri': redirect_url,
                'code': code,
            }
        ) as response:
            res = await response.json()
            print(f"{res=}")
