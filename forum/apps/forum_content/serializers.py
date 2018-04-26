from rest_framework import serializers

from .models import NoticeModel, CategoryModel, UserPostDetail, ReplyModel


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeModel
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyModel
        fields = '__all__'


class PostsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    reply = ReplySerializer(many=True)

    class Meta:
        model = UserPostDetail
        fields = '__all__'