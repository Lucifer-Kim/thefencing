from django.db import models

from django.utils import timezone


class FreePost(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


"""
class News(models.Model):
    title = models.CharField(max_length=100)
    news_url = models.TextField()
"""