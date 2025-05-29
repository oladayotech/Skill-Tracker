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
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    goal = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.goal}"
    
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()