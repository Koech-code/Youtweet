from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = "")
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class CommentTweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = "")
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='commenttweet')
    body = models.CharField(max_length=1000, null=False)

class UploadVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = "")
    videoname = models.CharField(max_length=50)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    about = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.videoname

class CommentVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = "")
    uploadedvideo = models.ForeignKey(UploadVideo, on_delete=models.CASCADE, related_name='commentvideo')
    body = models.CharField(max_length=1000, null=False)