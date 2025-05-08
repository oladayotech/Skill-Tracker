from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    journal_content = models.TextField()
    journal_image = models.ImageField(upload_to='journal_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

# class Journal(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     # journal_title = models.CharField(max_length=300)
#     journal_content = models.TextField()
#     journal_image = models.ImageField(null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

# models.py
class DailyLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.IntegerField()
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    log_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)