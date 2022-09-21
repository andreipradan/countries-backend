from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from users.models import Score

User = get_user_model()


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = "user", "score", "duration", "game_type", "game_sub_type", "created_at"
    readonly_fields = "created_at", "updated_at"


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        (
            "Telegram",
            {
                "fields": (
                    "telegram_id",
                    "telegram_notifications_active",
                    "telegram_notifications_silent",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display = ("email", "first_name", "last_name", "is_staff")
    search_fields = ("first_name", "last_name", "email")
    ordering = ("email",)

