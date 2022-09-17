from rest_framework.generics import ListCreateAPIView

from api.serializers.user import ScoreSerializer
from users.models import Score


class ScoreList(ListCreateAPIView):
    serializer_class = ScoreSerializer
    queryset = Score.objects.prefetch_related("user")
