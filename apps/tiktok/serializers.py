from rest_framework import serializers

from apps.tiktok.models import TikTokVideo, TikTokProfile, HashTag, SearchKeywords


class TikTokVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TikTokVideo
        fields = '__all__'


class TikTokProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = TikTokProfile
        fields = '__all__'


class HashTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashTag
        fields = '__all__'


class SearchKeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchKeywords
        fields = '__all__'


class TiktokContentSerializer(serializers.ModelSerializer):
    user = TikTokProfileSerializer(read_only=True)
    hashtag = HashTagSerializer(read_only=True)
    search_keyword = HashTagSerializer(read_only=True)

    class Meta:
        model = TikTokVideo
        fields = '__all__'
