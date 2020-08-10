from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostBlog, CommentBlog
from django.utils import timezone
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DetailView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostBlogForm, CommentsBlogForm
from django.contrib.auth.decorators import login_required
# Create your views here.

#create Home Page
class HomePage(TemplateView):
  template_name = "core/about.html"

class PostBlogListView(ListView):
  queryset = PostBlog.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")
  template_name = "core/index.html"
  def get_queryset(self, *args, **kwargs):
    return PostBlog.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")

class PostBlogDetail(DetailView):
  template_name = "core/post_detail.html"

  def get_object(self, *args, **kwargs):
    slug = self.kwargs.get("slug")
    instance = PostBlog.objects.get(slug= slug)
    return instance


class PostBlogCreate(LoginRequiredMixin, CreateView):
  login_url = "/login/"
  redirect_field_name = "core/post_detail.html"
  form_class = PostBlogForm
  model = PostBlog

class PostBlogUpdate(LoginRequiredMixin, UpdateView):
  login_url = "/login/"
  redirect_field_name = "core/post_detail.html"
  form_class = PostBlog
  model = PostBlog

class PostBlogDelete(LoginRequiredMixin, DetailView):
  login_url = "/login/"
  model = PostBlog
  success_url = "/"


class PostBlogDraft(LoginRequiredMixin, ListView):
  login_url = "/login/"
  redirect_field_name = "core/index.html"
  model = PostBlog

  def get_queryset(self, *args, **kwargs):
    return PostBlog.objects.filter(published_date__isnull=True).order_by("create_data")


####################################################CommentBlog############################

#-->add comment to post
@login_required
def post_comment(requset, slug, *args, **kwargs):
  slug = requset.kwargs.get("slug")
  template_name = "core/comment_form.html"
  post = get_object_or_404(PostBlog, slug=slug)

  if requset.method == "POST":
    form = CommentBlog(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.post = post
      comment.save()
      return redirect("core/post_detail.html", slug=slug)
    
    else:
      form = CommentBlog()
    
    return render(requset,template_name, {"form":form})


#--> approved cooment
@login_required
def approve_comment(request, pk, *args, **kwargs):
  comment = get_object_or_404(CommentBlog, pk=pk)
  comment.approved()

  return redirect("post-details", pk=comment.post.slug)

@login_required
def remove_comment(request, pk):
  comment = get_object_or_404(CommentBlog, pk=pk)
  slug    = comment.post.slug
  comment.delete()
  return redirect("post-details", pk=slug)
  
