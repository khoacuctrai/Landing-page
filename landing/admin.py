from django.contrib import admin
from .models import Registration

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'city', 'registered_at')
    search_fields = ('full_name', 'phone', 'email', 'city')
    list_filter = ('city', 'registered_at')
