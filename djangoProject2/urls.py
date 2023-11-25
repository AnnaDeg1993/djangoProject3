from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include

from djangoProject2 import settings
from news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', views.about),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

