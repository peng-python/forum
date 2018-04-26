from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserRegSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label='用户名', help_text='用户名', required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message='用户已存在')])
    password = serializers.CharField(style={'input_type': 'password'}, help_text='密码', label='密码', write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')


class UserDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(label='昵称', help_text='昵称', required=True, allow_blank=False,
                                 validators=[UniqueValidator(queryset=User.objects.all(), message='用户名已存在')])
    image = serializers.ImageField(label='用户头像', help_text='用户头像', required=True)

    class Meta:
        model = User
        fields = ('name', 'image')