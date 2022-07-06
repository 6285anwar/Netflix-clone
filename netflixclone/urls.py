"""netflixclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from netflix import views
from django.contrib import admin
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$', views.login, name='login'),
 
# ADMIM
    re_path(r'^admin_logout/$', views.admin_logout,name='admin_logout'),
    re_path(r'^admin_index/$', views.admin_index, name='admin_index'),
    re_path(r'^admin_home/$', views.admin_home, name='admin_home'),
    re_path(r'^admin_users/$', views.admin_users, name='admin_users'),
    re_path(r'^admin_adduser/$', views.admin_adduser, name='admin_adduser'),
    re_path(r'^admin_movie/$', views.admin_movie, name='admin_movie'),
    re_path(r'^admin_addmovie/$', views.admin_addmovie, name='admin_addmovie'),
    re_path(r'^admin_viewuser/(?P<id>\d+)/$', views.admin_viewuser, name='admin_viewuser'),

# USER

    re_path(r'^user_logout/$', views.user_logout,name='user_logout'),
    re_path(r'^user_index/$', views.user_index, name='user_index'),
    re_path(r'^user_home/$', views.user_home, name='user_home'),





    

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)