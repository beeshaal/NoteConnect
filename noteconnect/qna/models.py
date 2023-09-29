from django.db import models
from django.contrib.auth.models import User 


class Post(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)  
    uploaded_on = models.DateTimeField(auto_now_add=True)
    course = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
