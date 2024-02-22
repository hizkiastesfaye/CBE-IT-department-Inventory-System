from django.db import models
from store.models import Items

# Create your models here.

class User(models.Model):

    fullname =models.CharField(max_length=50)
    username=models.CharField(max_length=25,unique=True)
    email=models.EmailField()
    responsibility=models.CharField(max_length=40)
    password=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.username}-{self.responsibility}'
    
class Request(models.Model):
    username=models.CharField(max_length=50)
    item= models.CharField(max_length=50, null=True)
    quantity=models.PositiveIntegerField()
    reason=models.TextField()
    date=models.DateTimeField(auto_now_add=True,editable=True)
    userRequest=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    is_approved=models.BooleanField(default=False,null=True)

    def __str__(self):
        return f'{self.username}'
    
class staffDescription(models.Model):
    username=models.CharField(max_length=50)
    description = models.TextField()
    date=models.DateTimeField(auto_now_add=True,editable=True)
    userRequest=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.username}'
