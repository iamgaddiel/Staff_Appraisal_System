from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # SCH/FCULT/DPT/LC/12345678
    # SCH/FCULT/DPT/SD/12345678

    ACCOUNT_TYPE = [
        ("student", "student"),
        ("student", "student"),
    ]
    id = models.UUIDField(unique=True, primary_key=True, )
    school_id = models.CharField(max_length=25, unique=True)
    dob = models.DateField()
    faculty = models.CharField(max_length=20)  
    department = models.CharField(max_length=20)
    account_type = models.CharField(max_length=10)

    USERNAME_FIELD = "school_id"
    REQUIRED_FIELDS = []


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='profile.jpg', upload_to='profile_images')

    def __str__(self) -> str:
        return "{0} {1}'s profile".format(
            self.user.first_name, 
            self.user.last_name
        )


class Lecturer(models.Model):
    ACADEMIC_RANK = (
        ("", "")
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    academic_rank = models.CharField(max_length=20, choices=ACADEMIC_RANK)

    def __str__(self) -> str:
        return f"lecturer {self.user.first_name} {self.user.last_name}"