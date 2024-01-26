
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.forms import  ModelForm
from django.urls import reverse
from django.utils import timezone



# Create your models here.
class Task (models.Model):
    title = models.CharField(max_length=50)
    time_start = models.TimeField(auto_now_add=True)
    date_finish = models.DateTimeField(default=timezone.now())
    color = models.FloatField()
    text = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_info', kwargs={'task_id': self.pk})

class Category (models.Model):
    name = models.CharField(max_length=50, db_index=True)
    def __str__(self):
        return self.name