from django.contrib import admin
from .models import SecretMessage


@admin.register(SecretMessage)
class SecretMessageAdmin(admin.ModelAdmin):
    '''Admin View for SecretMessage'''

    list_display = ('id', 'message', 'slug')
