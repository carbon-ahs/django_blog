from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    phone_number = models.CharField(_("Phone Number"), max_length=30)
