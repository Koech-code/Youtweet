from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from . models import Tweet, CommentTweet, UploadVideo, CommentVideo


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('user', 'video', 'content', 'image', 'timestamp')

class CommentTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentTweet
        fields = ('user', 'tweet', 'body')

class CommentVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentVideo
        fields = ('user', 'uploadedvideo', 'body')

class UploadVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadVideo
        fields = ('user', 'videoname', 'video', 'about')        