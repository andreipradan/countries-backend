from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    ordering = 'email',
