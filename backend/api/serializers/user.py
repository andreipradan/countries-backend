from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from users.models import User


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
            "password",
            "password2",
            "telegram_id",
            "telegram_notifications_active",
            "telegram_notifications_silent",
        )
    password = serializers.CharField(
        required=True,
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )
    password2 = serializers.CharField(
        required=True,
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )

    def validate(self, data):
        password2 = data.pop("password2")
        if data["password"] != password2:
            raise serializers.ValidationError("passwords must match")

        user = User(**data)
        password = data.get("password")
        errors = {}
        try:
            validate_password(password=password, user=user)
        except ValidationError as e:
            errors['password'] = list(e.messages)
        if errors:
            raise serializers.ValidationError(errors)
        return super().validate(data)

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
