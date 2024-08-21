import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Sport(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Member(AbstractUser):
    SPORT_CHOICES = [
        ("running", "Course à pied"),
        ("cycling", "Vélo"),
        ("swimming", "Natation")
    ]

    GENDER_CHOICES = [
        ('male', 'Homme'),
        ('female', 'Femme'),
    ]
    birth = models.DateField(null=True, blank=True, default=datetime.date.fromtimestamp(0000000000000))
    weight = models.IntegerField(default=0)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='male')
    height = models.IntegerField(default=0)
    sports = models.ManyToManyField(Sport, related_name="users")
    is_coach = models.BooleanField(default=False, null=True, blank=True)
    coach_selected = models.BooleanField(default=False, null=True, blank=True)
    athlete_profile_completed = models.BooleanField(default=False, null=False, blank=True)
