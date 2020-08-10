from django import forms
from .models import PostBlog, CommentBlog
from tinymce.widgets import TinyMCE

#create PostBlogForm
class PostBlogForm(forms.ModelForm):
  class Meta:
    model   = PostBlog
    fields  = ("author", "title", "description", "slug", "create_data", "published_date")

    widgets = {
      "title": forms.TextInput(attrs={"class":"input-text", "placeholder":"Enter your title"}),
      "description": TinyMCE(attrs={"col":500, "rows":10, "class": "form-control"})
    }

#Create CommentBlogForm
class CommentsBlogForm(forms.ModelForm):
  class Meta:
    model   = CommentBlog
    fields  = ("author", "text")
    
    widgets = {
      "author":forms.TextInput(attrs={"class":"input-text", "placeholder":"Enter your name"}),
      "text":forms.Textarea(attrs={"class":"editable meduim-editor-textarea comment"})
    }