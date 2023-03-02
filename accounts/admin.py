from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'email',
                    'first_name', 'last_name', 'age', 'is_staff']
    add_fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )
