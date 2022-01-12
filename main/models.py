from django.db import models

# Create your models here.


class SecretMessage(models.Model):
    """Model definition for SecretMessage."""

    message = models.TextField()

    class Meta:
        """Meta definition for SecretMessage."""

        verbose_name = 'Secret Message'
        verbose_name_plural = 'Secret Messages'

    def __str__(self):
        """Unicode representation of SecretMessage."""
        return 'Model Name: Secret Message'
