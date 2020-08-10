from django.urls import path, re_path, include
from .views import (HomePage, PostBlogListView, PostBlogDetail, PostBlogCreate, PostBlogUpdate, PostBlogDelete, PostBlogDraft, post_comment, approve_comment, remove_comment)
app_name = "core"

urlpatterns = [
  #--> paths for PostBlog model
  path("about/", HomePage.as_view(), name="home-page"),
  path("", PostBlogListView.as_view(), name="articles"),
  re_path(r'post/(?P<slug>[\w-]+)/$', PostBlogDetail.as_view(), name="post-details"),
  path("post/new/", PostBlogCreate.as_view(), name="create-post"),
  re_path(r"post/update/(?P<slug>[\w-]+)/$", PostBlogUpdate.as_view(), name="update-post"),
  re_path(r"post/delete/(?P<slug>[\w-]+)/$", PostBlogDelete.as_view(), name="delete-post"),
  path("post/draft/", PostBlogDraft.as_view(), name="draft-post"),


  #--> paths for CommentBlog model
  re_path(r"post/comment/(?P<slug>[\w-]+)/$", post_comment, name="add-post-comment"),
  re_path(r"post/approve/(?P<pk>[\w-]+)/$", approve_comment, name="approve-comment"),
  re_path(r"post/delete/(?P<pk>[\w-]+)/$", remove_comment, name="remove-comment"),
]