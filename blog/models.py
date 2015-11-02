from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Post(models.Model):
    """
    Model for blog post .....
    """
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    text = models.TextField()
    published_date = models.DateTimeField(
            blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, related_name='comments')
