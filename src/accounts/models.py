from django.db import models
from django.contrib.auth.forms import UsernameField, SetPasswordForm
from django.contrib.auth.management.commands.createsuperuser import PASSWORD_FIELD

# Create your models here.
class CustomUser(models.Model):
    username=UsernameField()
    password=SetPasswordForm