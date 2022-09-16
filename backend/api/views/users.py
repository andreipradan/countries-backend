from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView

from api.serializers import UserSerializer
from api.serializers.user import ScoreSerializer
from users.models import User


class UserList(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.prefetch_related("scores")


class UserDetail(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.prefetch_related("scores")


class UserScore(CreateAPIView):
    serializer_class = ScoreSerializer
