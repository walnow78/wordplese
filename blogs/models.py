from blogs.validators import badwords_detector
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Post(models.Model):
    owner = models.ForeignKey(User)
    title = models.TextField(max_length=25, default="", validators=[badwords_detector])
    resume = models.TextField(max_length=100, default="")
    content = models.TextField(default="")
    url = models.URLField(blank=True, default="")
    publication_date = models.DateTimeField(blank=True, null=True, default="")
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
