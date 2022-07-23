from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from core.utils import generate_password, generate_shool_id, get_password
from .models import CustomUser, Profile
from student.models import Student


@receiver(signal=pre_save, sender=CustomUser)
def add_user_values(sender, instance, *args, **kwargs):
    instance.school_id = generate_shool_id(8)
    if instance.account_type == "student":
      hashed_password = generate_password(instance.password)
      instance.password = hashed_password
      
      
@receiver(post_save, sender=CustomUser)
def create(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)
    if instance.account_type == "student":
        Student.objects.create(user=instance)
