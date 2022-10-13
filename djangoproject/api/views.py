from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Tweet
from .serializers import TweetSerializer


@api_view(['GET', 'POST'])
def tweet(request):
    """
    List all tweets, or create a new one.
    """
    if request.method == 'GET':
        tweets = Tweet.objects.all().order_by('created_at', 'name')
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
