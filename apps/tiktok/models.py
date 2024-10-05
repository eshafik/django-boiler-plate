from django.db import models


# Create your models here.
class TikTokProfile(models.Model):
    user = models.OneToOneField('user.User', on_delete=models.DO_NOTHING,
                                related_name='titok_profile')
    nick_name = models.CharField(max_length=255, blank=True, null=True)
    follower_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    bio_info = models.CharField(max_length=255, blank=True, null=True)
    profile_link = models.URLField(null=True, blank=True)


class HashTag(models.Model):
    tag = models.CharField(max_length=255, unique=True)
    video_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)


class SearchKeywords(models.Model):
    search_text = models.CharField(max_length=255)
    video_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)


class TikTokVideo(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.DO_NOTHING, related_name='user_videos')
    description = models.TextField(blank=True, null=True)
    hashtag = models.ForeignKey(HashTag, on_delete=models.DO_NOTHING,
                                related_name='hashtag_videos',
                                blank=True, null=True)
    search_keyword = models.ForeignKey(SearchKeywords, on_delete=models.DO_NOTHING,
                                       related_name='search_keyword_videos',
                                       blank=True, null=True)
    comment_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    video_url = models.URLField(null=True, blank=True, max_length=500)

