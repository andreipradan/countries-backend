from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from users.models import User, Score


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "id", "email", "first_name", "last_name", "password", "password2"

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
        if self.instance:
            return super().validate(data)

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


class ScoreSerializer(ModelSerializer):
    class Meta:
        model = Score
        fields = "__all__"

    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField()
