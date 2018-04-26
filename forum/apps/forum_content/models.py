from django.db import models
from datetime import datetime

from DjangoUeditor.models import UEditorField
from users.models import UserProfile

# Create your models here.


class NoticeModel(models.Model):
    title = models.CharField(max_length=30, verbose_name='公告名称')
    content = UEditorField(default='', imagePath='forum/content/notice/', filePath='forum/content/notice',
                           width=1000, height=300, verbose_name='公告内容')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '版块公告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class CategoryModel(models.Model):
    name = models.CharField(max_length=4, default='', verbose_name='类别')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserPostDetail(models.Model):
    title = models.CharField(max_length=30, verbose_name='标题')
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    content = UEditorField(default='', imagePath='forum/content/post/', filePath='forum/content/post/',
                           width=1000, height=300, verbose_name='帖子内容')
    is_essence = models.BooleanField(default=False, verbose_name='是否为精华')
    category = models.ForeignKey(CategoryModel, verbose_name='类别')
    read_nums = models.IntegerField(default=0, verbose_name='阅读数')
    reply_nums = models.IntegerField(default=0, verbose_name='回复数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '帖子内容'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ReplyModel(models.Model):
    reply_title = models.ForeignKey(UserPostDetail, verbose_name='回复对应文章', related_name='reply')
    reply_content = UEditorField(default='', imagePath='forum/content/post/', filePath='forum/content/post/',
                                 width=1000, height=300, verbose_name='回复内容')
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '回复内容'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.reply_title.title