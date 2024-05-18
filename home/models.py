# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Salary(models.Model):

    #__Salary_FIELDS__
    class = models.CharField(max_length=255, null=True, blank=True)

    #__Salary_FIELDS__END

    class Meta:
        verbose_name        = _("Salary")
        verbose_name_plural = _("Salary")


class Calstr(models.Model):

    #__Calstr_FIELDS__
    employee = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    class = models.CharField(max_length=255, null=True, blank=True)

    #__Calstr_FIELDS__END

    class Meta:
        verbose_name        = _("Calstr")
        verbose_name_plural = _("Calstr")


class Earnings(models.Model):

    #__Earnings_FIELDS__
    employee = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    date = models.CharField(max_length=255, null=True, blank=True)
    experience = models.CharField(max_length=255, null=True, blank=True)

    #__Earnings_FIELDS__END

    class Meta:
        verbose_name        = _("Earnings")
        verbose_name_plural = _("Earnings")


class Teams(models.Model):

    #__Teams_FIELDS__
    team = models.CharField(max_length=255, null=True, blank=True)
    unified school district = models.CharField(max_length=255, null=True, blank=True)

    #__Teams_FIELDS__END

    class Meta:
        verbose_name        = _("Teams")
        verbose_name_plural = _("Teams")


class User(models.Model):

    #__User_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    team = models.CharField(max_length=255, null=True, blank=True)
    access = models.CharField(max_length=255, null=True, blank=True)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")



#__MODELS__END
