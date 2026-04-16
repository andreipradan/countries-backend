from datetime import datetime, timedelta, timezone

from rest_framework.authtoken.models import Token

TOKEN_EXPIRES_AFTER_SECONDS = 3600


class APIToken(Token):
    @property
    def expires_at(self):
        return self.created + timedelta(seconds=TOKEN_EXPIRES_AFTER_SECONDS)

    @property
    def is_expired(self):
        utc_now = datetime.now(timezone.utc)
        expiry = self.created + timedelta(seconds=TOKEN_EXPIRES_AFTER_SECONDS)
        return utc_now > expiry
