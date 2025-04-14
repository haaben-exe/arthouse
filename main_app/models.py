from django.db import models
from django.urls import reverse


class Post(models.Model):

    title = models.CharField(
        max_length=50, 
        blank=True
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