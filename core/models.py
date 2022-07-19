from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import messages
from django.http import HttpRequest

from core.utils import generate_password, generate_shool_id


class CustomUser(AbstractUser):
    # SCH/FCULT/DPT/LC/12345678
    # SCH/FCULT/DPT/SD/12345672

    ACCOUNT_TYPE = [
        ("student", "student"),
        ("lecturer", "lecturer"),
    ]
    
    id = models.UUIDField(unique=True, primary_key=True, default=uuid4, editable=False)
    school_id = models.CharField(max_length=43, unique=True, blank=True)
    dob = models.DateField(null=True)
    faculty = models.CharField(max_length=20, default='')  
    department = models.CharField(max_length=20, default='')
    name = models.CharField(max_length=30, default='')
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE, null=True)

    USERNAME_FIELD = "school_id"
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return f"{self.username} | {self.school_id}"


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='profile.jpg', upload_to='profile_images')

    def __str__(self) -> str:
        return "{0}'s profile".format(
            self.user.name, 
        )
