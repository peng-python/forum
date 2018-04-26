# import xadmin
#
# from .models import NoticeModel,CategoryModel,UserPostDetail,ReplyModel
#
#
# class NoticeAdmin(object):
#     list_display = ['title', 'content', 'add_time']
#     list_filter = ['title', 'content']
#     search_fields = ['title', 'content', 'add_time']
#     style_fields = {'content': 'ueditor'}
#
#
# class CategoryAdmin(object):
#     list_display = ['name', 'add_time']
#     list_filter = ['name']
#     search_fields = ['name', 'add_time']
#
#
# class UserPostDetailAdmin(object):
#     list_display = ['title', 'user', 'content', 'is_essence', 'category', 'read_nums', 'reply_nums', 'add_time']
#     list_filter = ['title', 'user', 'content', 'is_essence', 'category', 'read_nums', 'reply_nums']
#     search_fields = ['title', 'user', 'content', 'is_essence', 'category', 'read_nums', 'reply_nums', 'add_time']
#     style_fields = {'content': 'ueditor'}
#
#
# class ReplyAdmin(object):
#     list_display = ['reply_content', 'reply_title', 'user', 'add_time']
#     list_filter = ['reply_content', 'reply_title', 'user']
#     search_fields = ['reply_content', 'reply_title', 'user', 'add_time']
#     style_fields = {'content': 'ueditor'}
#
#
# xadmin.site.register(NoticeModel, NoticeAdmin)
# xadmin.site.register(CategoryModel, CategoryAdmin)
# xadmin.site.register(UserPostDetail, UserPostDetailAdmin)
# xadmin.site.register(ReplyModel, ReplyAdmin)