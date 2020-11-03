from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
  list_display = ['title', 'subTitle', 'fullName', 'categories', 'deleted']
  search_fields = ['title', 'subTitle']

  # def get_queryset(self, request):
  #   return Post.objects.filter(deleted = False)


admin.site.register(Post, PostAdmin)
