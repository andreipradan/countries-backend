from datetime import datetime, timedelta

import pytz
from rest_framework.authtoken.models import Token

TOKEN_EXPIRES_AFTER_SECONDS = 3600


class APIToken(Token):
    @property
    def expires_at(self):
        return self.created + timedelta(seconds=TOKEN_EXPIRES_AFTER_SECONDS)

    @property
    def is_expired(self):
        utc_now = datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)

        expiry = self.created + timedelta(seconds=TOKEN_EXPIRES_AFTER_SECONDS)
        return utc_now > expiry
