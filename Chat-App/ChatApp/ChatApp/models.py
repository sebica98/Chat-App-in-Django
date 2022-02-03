from datetime import datetime
from django.db import models
from django.contrib.auth.models import Permission, User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    photo = models.ImageField(null=True)

    def __str__(self):
        return self.address

class Message(models.Model):
    content = models.TextField(max_length=10000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default = datetime.now, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **args):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
