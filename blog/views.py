from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Post


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def posts(request):
    posts = Post.objects.filter(
        published_at__isnull=False).order_by('-published_at')
    post_list = serializers.serialize('json', posts)
    return HttpResponse(post_list, content_type="text/json-comment-filtered")
