from datetime import datetime
from email.utils import format_datetime
from django.db import models
from django.contrib.auth.models import Permission, User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    address = models.TextField()
    photo = models.ImageField(null=True, upload_to='images/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.user} {self.address}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(Profile, self).save(*args, **kwargs)


class Message(models.Model):
    content = models.TextField(max_length=10000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add= True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **args):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
