from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User



class Post(models.Model):

    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        null=True
        )
    title = models.CharField(
        max_length=50, 
        blank=True
        )
    image = models.ImageField(
        upload_to='post_images/', 
        blank=True, 
        null=True
        )
    category = models.CharField(
        max_length=40, 
        default='Global'
        )
    description = models.TextField(
        max_length=1000, 
        default='No description provided.', 
        blank=True
        )
    tags = models.CharField(
        max_length=25, 
        blank=True
        )
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'post_id': self.id})



class Comments(models.Model):

    author = models.ForeignKey(
        'auth.User', 
        on_delete=models.CASCADE,
        null=True,
        blank=True
        )
    text = models.CharField(
        max_length=500, 
        blank=True
        )
    date = models.DateField(
        auto_now_add=True
        )
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, 
        related_name='comments'
        )

    def __str__(self):
        return f"Comment on {self.post.title} at {self.date}"


