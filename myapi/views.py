from rest_framework import viewsets
from .serializers import PostsSerializer
from .models import Posts
import requests
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by('title')
    serializer_class = PostsSerializer


def home(request):
    response = requests.get('http://127.0.0.1:8000/posts/')
    data = response.json()
    return render(request, 'home.html', {'data': data})

@api_view(['DELETE'])
def postDelete(request, pk):
	posts = Posts.objects.get(id=pk)
	posts.delete()

	return Response('Item succsesfully delete!')
    
    
