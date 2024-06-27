from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student
from rest_framework.authtoken.models import Token
from django.conf import settings


@receiver(post_save , sender=settings.AUTH_USER_MODEL)
def create_post_signal(sender, instance=None, created=False, **kwargs):  
    if created:
        Token.objects.create(user=instance)