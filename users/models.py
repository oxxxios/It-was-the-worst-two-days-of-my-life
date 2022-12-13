from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from users.managers import MyUserManager


class User(AbstractBaseUser, PermissionsMixin):
    photo = models.ImageField(upload_to="media/", verbose_name="Фото профиля", blank=True)
    first_name = models.CharField(verbose_name="Имя", max_length=60)
    last_name = models.CharField(max_length=70, verbose_name="Фамилия")
    phone = PhoneNumberField(verbose_name="Номер телефона", unique=True, blank=True)
    is_staff = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = MyUserManager()

    def __str__(self) -> str:
        return self.first_name