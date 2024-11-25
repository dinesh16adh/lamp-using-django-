from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.CharField(max_length=500, null=True, blank=True)
    links = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    description = models.TextField(default="hello world")

    class Meta:
        verbose_name_plural = "More Blogs"

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comment")
    text = models.TextField()

    def __str__(self):
        # return self.text[:50]
        return f"{self.blog.title}'s comment"


# class Like(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="likes")
