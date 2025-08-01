import urllib.parse
import secrets

from src.config import settings
from src.state_storage import state_storage


def generate_google_oauth_redirect_uri(func) -> str:
    random_state = secrets.token_urlsafe(16)
    state_storage.add(random_state)

    query_params = {
        'client_id': settings.OAUTH_GOOGLE_CLIENT_ID,
        'redirect_uri': func(path='/auth/google'),
        'response_type': "code",
        'scope': " ".join ([
            "https://www.googleapis.com/auth/calendar",
            "https://www.googleapis.com/auth/drive",
            "openid",
            "profile",
            "email"
        ]),
        'access_type': "offline",
        'state': random_state,
    }
    query_string = urllib.parse.urlencode(query_params, quote_via=urllib.parse.quote)
    base_url: str = "https://accounts.google.com/o/oauth2/v2/auth"
    return f"{base_url}?{query_string}"
