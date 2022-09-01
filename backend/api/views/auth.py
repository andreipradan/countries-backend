from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import UserSerializer
from api.serializers import APITokenSerializer
from users.models import User


class APILogin(APIView):
    permission_classes = ()
    serializer_class = APITokenSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs["context"] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def get_serializer_context(self):
        return {
            "request": self.request,
            "format": self.format_kwarg,
            "view": self
        }

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        user = User.objects.get(pk=serializer.validated_data["user"].pk)
        return Response(
            {
                "expires_at": token.expires_at,
                "token": token.key,
                "user": UserSerializer(user).data,
            }
        )
