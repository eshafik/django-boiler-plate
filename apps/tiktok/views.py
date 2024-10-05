from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.tiktok.helpers import flatten_videos
from apps.tiktok.models import TikTokVideo
from apps.tiktok.serializers import TiktokContentSerializer


class TikTokListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TiktokContentSerializer
    permission_classes = [AllowAny]
    queryset = TikTokVideo.objects.select_related('user', 'hashtag', 'search_keyword').all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'hashtag__tag', 'search_keyword__text', 'user__username']

    def create(self, request, *args, **kwargs):
        hashtag_data = request.data.get('hashtag')
        keyword_search_data = request.data.get('search_keyword')
        data = flatten_videos(data=request.data)
        print(data)
        return Response({'message': 'Ok'})
