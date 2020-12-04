from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )

class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True,)
    age = models.IntegerField(null=True)
    contact = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    estate = models.ForeignKey('Hood', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'profiles'
        ordering = ['-name']

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


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=250)
    tag = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey('Hood', on_delete=models.CASCADE, related_name='hoods', default=1)

    class Meta:
        db_table = 'posts'
        ordering = ['-title']

    def __repr__(self):
        return f'{self.title}'

    @classmethod
    def search_posts(cls, searchTerm):
        posts = cls.objects.filter(title__icontains=searchTerm)
        return posts

class Hood(models.Model):
    Name = models.CharField(max_length=32)
    location = models.CharField(max_length=150)
    Count = models.IntegerField()
    Foreignkey = models.IntegerField()
    class Meta:
        db_table = 'Hood'
        ordering = ['-Name']

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def search_hood(cls, searchTerm):
        hoods = cls.objects.filter(name__icontains=searchTerm)
        return hoods

    @classmethod
    def search_by_title(cls, search_term):
        hoods = cls.objects.filter(name__icontains=search_term)
        return hoods

