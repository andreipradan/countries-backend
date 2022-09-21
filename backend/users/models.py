from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    telegram_id = models.CharField(max_length=32, blank=True, null=True)
    telegram_notifications_active = models.BooleanField(default=False)
    telegram_notifications_silent = models.BooleanField(default=False)

    username = None
    objects = UserManager()

    REQUIRED_FIELDS = ()
    USERNAME_FIELD = "email"

    @property
    def full_name(self):
        return self.get_full_name() or self.email

    def __str__(self):
        return self.full_name


class Score(models.Model):
    class Meta:
        ordering = "game_type", "game_sub_type", "-score", "duration"

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='scores'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    score = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    game_type = models.IntegerField(
        choices=(
            (1, "Random Map"),
            (2, "Free Guessing"),
        ),
        default=1,
    )
    game_sub_type = models.IntegerField(
        choices=(
            (1, "World"),
            (2, "North America"),
            (3, "South America"),
            (4, "Europe"),
            (5, "Africa"),
            (6, "Asia"),
            (7, "Oceania"),
        ),
        default=1,
    )
