import urllib.parse
from src.config import settings


def generate_google_oauth_redirect_uri() -> str:
    port = "" if settings.IS_CONTAINER else ":5173"
    query_params = {
        'client_id': settings.OAUTH_GOOGLE_CLIENT_ID,
        'redirect_uri': f"http://localhost{port}/auth/google",
        'response_type': "code",
        'scope': " ".join ([
            "https://www.googleapis.com/auth/calendar",
            "https://www.googleapis.com/auth/drive",
            "openid",
            "profile",
            "email"
        ]),
        'access_type': "offline",
        #state: ...
    }
    query_string = urllib.parse.urlencode(query_params, quote_via=urllib.parse.quote)
    base_url: str = "https://accounts.google.com/o/oauth2/v2/auth"
    return f"{base_url}?{query_string}"
