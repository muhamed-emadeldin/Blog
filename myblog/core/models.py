from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.db.models.signals import post_save, pre_save
from myblog.utilities.utils_nav import unique_slug_generator_pages
# Create your models here.

#create PostBlog class
class PostBlog(models.Model):

  #--> create fields in db
  author        = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="users")
  title         = models.CharField(max_length=200)
  description   = models.TextField()
  slug          = models.SlugField(unique= True, blank=True, null=True)
  create_data   = models.DateTimeField(default= timezone.now)
  published_date  = models.DateTimeField(blank=True, null=True)

  #--> set puplish date
  def publish(self):
    self.published_date = timezone.now
    self.save()

  #--> create dynamic url
  def get_absolute_url(self):
    return reverse("core:post-details", kwargs={"slug":self.slug})

  #--> return with comments approved
  def approved_comment(self):
    return self.comments.filter(approved_comment=True)

  #--> name table
  def __str__(self):
    return self.title

#--> create automation slugs
def post_slug_reciver(sender, instance, *args, **kwargs):
  instance.slug = unique_slug_generator_pages(instance)

pre_save.connect(post_slug_reciver, sender=PostBlog)


# Create CommentBlog Class
class CommentBlog(models.Model):

   #--> create fields in db
   post               = models.ForeignKey(PostBlog, on_delete=models.CASCADE, related_name="comments")
   author             = models.CharField(max_length=200)
   text               = models.TextField()
   approved_comment   = models.BooleanField(default=False)  

   #--> approve comments
   def approved(self):
     self.approved_comment = True
     self.save()

    #--> return to home page after commit
   def get_absolute_url(self):
     return reverse("core:post-list", kwargs={pk:self.post.slug})

   #--> name table
   def __str__(self):
     return self.title