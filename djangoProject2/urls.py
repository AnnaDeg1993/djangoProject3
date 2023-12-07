from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include

from djangoProject2 import settings
from news import views
from news.views import contact, login, show_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('register/', views.reg, name='register'),
    path('bot/', views.bot),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

