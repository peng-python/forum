from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='昵称')
    image = models.ImageField(upload_to='user/image/', null=True, blank=True, verbose_name='用户头像')
    birthday = models.DateField(null=True, blank=True, verbose_name='出生日期')
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), verbose_name='性别')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号码')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='邮箱')
    posts_nums = models.IntegerField(default=0, verbose_name='发帖数')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username