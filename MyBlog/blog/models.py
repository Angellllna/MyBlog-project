from django.db import models
from django.utils import timezone
from datetime import timedelta


class Author(models.Model):
    name = models.CharField(max_length=120)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="posts",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    def published_recently(self) -> bool:
        now = timezone.now()
        return now - timedelta(days=7) <= self.published_date <= now


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    author_name = models.CharField(max_length=120)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author_name}: {self.text[:25]}"
