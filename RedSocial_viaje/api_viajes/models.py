from django.conf import settings
from django.db import models
import secrets
<<<<<<< HEAD

class Token(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='custom_auth_token'  # Cambia el related_name
    )
    key = models.CharField(max_length=40, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = secrets.token_hex(20)  # Genera un token aleatorio
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Token for {self.user.username}"



=======
>>>>>>> e431b4f308c4ade594ee16bd9b3b60f0b7ad5787

class Token(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='custom_auth_token'  # Cambia el related_name
    )
    key = models.CharField(max_length=40, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = secrets.token_hex(20)  # Genera un token aleatorio
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Token for {self.user.username}"
# Create your models here.
