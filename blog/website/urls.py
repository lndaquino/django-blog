from django.urls import path, include
from .views import helloBlog

urlpatterns = [
  path('', helloBlog),
]