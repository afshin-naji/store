
from django.db import models
from django.contrib.auth.models import User
from store.models import Product


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'نظر {self.text}. از {self.user}.'
    
    class Meta:
        ordering = ['created_time']
