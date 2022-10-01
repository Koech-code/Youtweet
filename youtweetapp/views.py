from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UploadVideoSerializer, CommentVideoSerializer, CommentTweetSerializer, TweetSerializer
from .models import CommentTweet, Tweet, CommentVideo, UploadVideo

# Create your views here.

@api_view(['POST'])
def create_tweet_view(request, *args, **kwags):
    '''
    Create a tweet
    '''

    serializers = TweetSerializer(data=request.data)

    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data,
        status=status.HTTP_201_CREATED)
    else:
        return Response(serializers.errors, 
        status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_tweet_view(request, *args, **kwags):
    '''
    See all tweets created by users
    '''
    tweets = Tweet.objects.all()
    serializetweets = TweetSerializer(tweets, many=True)
    
    return Response(serializetweets.data)

@api_view(['POST'])
def upload_video_view(request, *args, **kwags):
    '''
    Upload a video for other users to see and comment on.
    '''
    serializevideos = UploadVideoSerializer(data=request.data)

    if serializevideos.is_valid():
        serializevideos.save()
        return Response(serializevideos.data,
        status=status.HTTP_201_CREATED)
    else:
        return Response(serializevideos.errors, 
        status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_videos_view(request, *args, **kwags):
    '''
    See all videos uploaded by users
    '''
    videos = UploadVideo.objects.all()
    serializevideos = UploadVideoSerializer(videos, many=True)
    
    return Response(serializevideos.data)

@api_view(['POST'])
def comment_tweet_view(request, *args, **kwags):
    '''
    Comment on a tweet made by a Youtweet user
    '''
    serializer = CommentTweetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, 
        status=status.HTTP_201_CREATED)            
    else:
        return Response(serializer.errors, 
        status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def see_all_tweet_comments(request, id, *args, **kwags):
    '''
    See all comments made on a tweet
    '''
    commentedtweets = CommentTweet.objects.filter(tweet=id)
    serializetweetcomments = CommentTweetSerializer(commentedtweets, many=True)

    return Response(serializetweetcomments.data)

@api_view(['POST'])
def comment_video_view(request, *args, **kwags):
    '''
    Comment on a video uploaded by a Youtweet user
    '''
    serializer = CommentVideoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, 
        status=status.HTTP_201_CREATED)            
    else:
        return Response(serializer.errors, 
        status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def see_all_video_comments(request, pk, *args, **kwags):
    '''
    See all comments made on an uploaded video
    '''
    commentedvideos = CommentVideo.objects.filter(video_id=pk)
    serializevideocomments = CommentVideoSerializer(commentedvideos, many=True)

    return Response(serializevideocomments.data)

