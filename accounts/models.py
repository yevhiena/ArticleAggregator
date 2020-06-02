from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
        biology = models.BooleanField(default=False)
        cosmology = models.BooleanField(default=False)
        hi_tech = models.BooleanField(default=False)
        history = models.BooleanField(default=False)
        media = models.BooleanField(default=False)
        medicine = models.BooleanField(default=False)
        physics = models.BooleanField(default=False)
        psychology = models.BooleanField(default=False)
        sci_fi = models.BooleanField(default=False)

