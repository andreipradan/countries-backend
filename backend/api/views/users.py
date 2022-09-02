from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView

from api.serializers import UserSerializer
from users.models import User


class UserList(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects


class UserDetail(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects
