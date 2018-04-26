from django.shortcuts import render
from rest_framework import mixins, viewsets

from .models import UserPostDetail, CategoryModel, NoticeModel
from .serializers import PostsSerializer, CategorySerializer, NoticeSerializer

# Create your views here.


class PostsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = UserPostDetail.objects.all()
    serializer_class = PostsSerializer


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class NoticeViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = NoticeModel.objects.all().order_by('-id')
    serializer_class = NoticeSerializer