
from django.contrib import admin
from django.urls import path

from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.list, name = 'list'),
    path('detail/', views.detail, name = 'detail'),
]
