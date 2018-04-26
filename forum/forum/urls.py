"""forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.static import serve
from forum.settings import MEDIA_ROOT
import xadmin

# from rest_framework.authtoken import views
# from rest_framework.routers import DefaultRouter
# from rest_framework.documentation import include_docs_urls
# from rest_framework_jwt.views import obtain_jwt_token
#
# from users.views import UserViewSet,UserDetailViewSet
# from forum_content.views import PostsListViewSet,CategoryViewSet,NoticeViewSet
#
#
# router = DefaultRouter()
#
# router.register(r'users', UserViewSet, base_name='users')
# router.register(r'detail', UserDetailViewSet, base_name='detail')
# router.register(r'list', PostsListViewSet, base_name='list')
# router.register(r'categorys', CategoryViewSet, base_name='categorys')
# router.register(r'notice', NoticeViewSet, base_name='notice')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # url(r'^ueditor/', include('DjangoUeditor.urls')),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^', include(router.urls)),
    # url(r'^api-token-auth/', views.obtain_auth_token),
    # url(r'^login/', obtain_jwt_token),
    # url(r'docs/', include_docs_urls(title='论坛')),
]
