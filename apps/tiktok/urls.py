from django.urls import path

from apps.tiktok.views import TikTokListCreateAPIView

# Put here views here
urlpatterns = [
    path('data', TikTokListCreateAPIView.as_view()),
]
