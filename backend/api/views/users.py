from rest_framework.generics import ListAPIView

from api.serializers import UserSerializer
from users.models import User


class UserList(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects
