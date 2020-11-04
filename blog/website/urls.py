from django.urls import path, include
from .views import helloBlog, postDetail, saveForm

urlpatterns = [
  path('', helloBlog, name='blogHome'),
  path('post/<int:id>/', postDetail, name='postDetailURL' ),
  path('save-form/', saveForm, name='saveFormURL'),
]