from fastapi import Depends

from app.core.security import (
    oauth2_scheme,
    verify_access_token
)

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_access_token(token)

    return payload