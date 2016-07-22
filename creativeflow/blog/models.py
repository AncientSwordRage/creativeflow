from django.db import models  # NOQA
from django.utils import timezone

# Create your models here.

SOCIAL_MEDIA = [{"name": "Facebook",
                 "url": "https://www.facebook.com/Creative-flow-629727287042242"
                 }]


class Post(models.Model):
    """Model for a blog post."""

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(blank=True, null=True)

    class Meta: # NOQA
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        """To String Method."""
        return self.title

    # TODO: Define custom methods here
    def publish(self):
        """Method for publishing the blog post."""
        self.published = timezone.now()
        self.save()
