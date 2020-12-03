from django.contrib import admin
from .models import Profile,Business,Post,Hood
# Register your models here.
admin.site.register(Hood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Post)
