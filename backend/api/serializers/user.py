from rest_framework.serializers import ModelSerializer
from users.admin import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "date_joined",
            "email",
            "first_name",
            "full_name",
            "last_login",
            "last_name",
            "telegram_id",
            "telegram_notifications_active",
            "telegram_notifications_silent",
        )
