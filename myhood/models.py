from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='#', blank=True,)
    age = models.IntegerField(null=True)
    contact = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    estate = models.ForeignKey('hood', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'profiles'
        ordering = ['name']

    def __repr__(self):
        return f'{self.name}'

    @classmethod
    def search_profiles(cls, searchTerm):
        profiles = cls.objects.filter(name__icontains=searchTerm)
        return profiles

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(name=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()


class Business(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    location = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'businesses'
        ordering = ['-name']

    def __repr__(self):
        return f'{self.name}'

    @classmethod
    def search_biz(cls, searchTerm):
        biz = cls.objects.filter(name__icontains=searchTerm)
        return biz




