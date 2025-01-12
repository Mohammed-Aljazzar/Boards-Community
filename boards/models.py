from django.db import models
from django.contrib.auth.models import User
from django.db.models import ForeignKey
from django.utils.text import Truncator

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
    def get_posts_count(self):
        return Post.objects.filter(topic__board= self).count()
    
    def get_last_post(self):
        return Post.objects.filter(topic__board= self).order_by('-created_dt').first()

class Topic(models.Model):
    subject = models.CharField(max_length=250)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topics')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')
    created_dt = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    updated_by = models.ForeignKey(User,related_name='+',on_delete=models.CASCADE,null=True)
    updated_dt = models.DateTimeField(null=True,auto_now=True)
    
    def __str__(self):
        return self.subject
    
    class Meta:
        ordering = ['-created_dt']


class Post(models.Model):
    message = models.TextField(max_length=1000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User,related_name='+',on_delete=models.CASCADE,null=True)
    updated_dt = models.DateTimeField(null=True)
    


    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)