from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save 
from django.dispatch import receiver
# Create your models here.

class UserProfile(models.Model):
    user= models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    profile_picture = models.ImageField( upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.user.username
 
@receiver(post_save, sender=User)   
def create_userprofile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User) 
def save_userprofile(sender, instance, **kwargs):
    try:
        instance.profile.save()  # This should be `instance.profile` instead of `instance.userprofile`
    except UserProfile.DoesNotExist:
        pass  # Handle the case where the profile does not exist

