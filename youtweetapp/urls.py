from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    create_tweet_view,
    get_tweet_view,
    upload_video_view,
    get_videos_view,
    comment_tweet_view,
    comment_video_view,
    see_all_video_comments,
    see_all_tweet_comments,
)

urlpatterns = [
    path('createtweet/', create_tweet_view),
    path('getweet/', get_tweet_view),
    path('uploadvideos/', upload_video_view),
    path('getvideos/', get_videos_view),
    path('commentweet/', comment_tweet_view),
    path('videocomments/<int:pk>/', see_all_video_comments),
    path('commentvideo/', comment_video_view),
    path('tweetcomments/<int:id>/', see_all_tweet_comments),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)