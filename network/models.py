from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime  

class User(AbstractUser):
    pass

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")

class Entity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now())

class Like(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")

class Post(models.Model):
    entity = models.OneToOneField(Entity, on_delete=models.CASCADE, related_name="post")

class Comment(models.Model):
    entity = models.OneToOneField(Entity, on_delete=models.CASCADE, related_name="comment")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")