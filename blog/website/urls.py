from django.urls import path, include
from .views import helloBlog, postDetail

urlpatterns = [
  path('', helloBlog, name='blogHome'),
  path('post/<int:id>', postDetail, name='postDetailURL' )
]