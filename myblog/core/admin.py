from django.contrib import admin
from .models import PostBlog, CommentBlog
from .forms import PostBlogForm, CommentsBlogForm
# Register your models here.

class PostBlogAdmin(admin.ModelAdmin):
  form = PostBlogForm
admin.site.register(PostBlog, PostBlogAdmin)
admin.site.register(CommentBlog)