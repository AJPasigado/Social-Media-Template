from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    date_created = models.DateTimeField("Date Created", auto_now_add=True)
    date_updated = models.DateTimeField("Date updated", auto_now=True)
    content = models.TextField()
    is_active = models.BooleanField()
    #defaults to True upon creation


    def __str__(self):
        return self.title

class Comment(models.Model):
    date_created = models.DateTimeField("Date Created", auto_now=False, auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
