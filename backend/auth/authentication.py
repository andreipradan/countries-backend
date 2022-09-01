from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

from auth.models import APIToken


class ExpiringTokenAuthentication(TokenAuthentication):
    model = APIToken

    def authenticate_credentials(self, key):
        user, token = super().authenticate_credentials(key)
        if token.is_expired:
            raise AuthenticationFailed("Token expired.")
        return user, token
