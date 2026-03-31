from django.contrib.auth.backends import ModelBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

from auth.models import APIToken


class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        from django.contrib.auth import get_user_model

        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None


class ExpiringTokenAuthentication(TokenAuthentication):
    model = APIToken

    def authenticate_credentials(self, key):
        user, token = super().authenticate_credentials(key)
        if token.is_expired:
            raise AuthenticationFailed("Token expired.")
        return user, token
