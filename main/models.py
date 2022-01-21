from django.db import models
import random, string

from django.db.models.fields import SlugField
# Create your models here.


class SecretMessage(models.Model):
    """Model definition for SecretMessage."""

    message = models.TextField()
    slug = models.SlugField(max_length=255)

    class Meta:
        """Meta definition for SecretMessage."""

        verbose_name = 'Secret Message'
        verbose_name_plural = 'Secret Messages'

    def __str__(self):
        """Unicode representation of SecretMessage."""
        return 'Model Name: Secret Message'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_generator()
            super(SecretMessage, self).save(*args, **kwargs)


def slug_generator():
    '''Generates random slug'''
    return ''.join(
        random.choices(string.ascii_lowercase + string.digits +
                       string.ascii_uppercase,
                       k=30))
