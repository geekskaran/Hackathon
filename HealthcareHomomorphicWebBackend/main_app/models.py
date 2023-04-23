from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from .manager import UserManager

# Create your models here.

class User(AbstractUser):
    username          = None
    email             = models.EmailField(unique=True, null=True)
    phone             = models.CharField(max_length=16,null=True,blank=True, unique=True , validators= [settings.MOBILE_REGEX_VALIDATOR])
    USERNAME_FIELD    = 'email'
    REQUIRED_FIELDS   = []
    
    objects = UserManager()
    
    def name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return f"ID:{self.id} || EMAIL:{self.email} || PHONE:{self.phone} "



class TbPatientInfo(models.Model):
    patient         =             models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    gender          =             models.CharField(max_length=45, blank=True, null=True)
    heart_rate      =             models.FloatField(blank=True, null=True)
    height          =             models.FloatField(blank=True, null=True)
    mass            =             models.FloatField(blank=True, null=True)
    sugar_level     =             models.FloatField(blank=True, null=True)
    hb_level        =             models.FloatField(blank=True, null=True)
    wbc_count       =             models.FloatField(blank=True, null=True)
    residual_volume =             models.FloatField(blank=True, null=True)
    vital_capcity   =             models.FloatField(blank=True, null=True)
    body_temp       =             models.FloatField(blank=True, null=True)


class TbPatientReport(models.Model):
    patient         =             models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    bmi             =             models.CharField(max_length=45, blank=True, null=True)
    is_fever        =             models.BooleanField(blank=True, null=True)
    total_lung_capacity  =        models.FloatField(blank=True, null=True)
