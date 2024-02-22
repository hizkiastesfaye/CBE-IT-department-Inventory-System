from django.db import models

# Create your models here.

class Items(models.Model):
    item = models.CharField(max_length=50)
    quantity=models.PositiveIntegerField()
    date=models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self):
        return f'{self.item}'
    