from django.contrib.auth.models import AbstractUser, User, AbstractBaseUser
from django.db import models


class Users(AbstractUser, AbstractBaseUser):
    User.USERNAME_FIELD = 'email'
    ROLE = [('SALES', 'Sales'),
            ('SUPPORT', 'Support'),
            ('MANAGEMENT', 'Management')
            ]

    role = models.CharField(default="Null", max_length=10, choices=ROLE)

    class Meta:
        verbose_name = 'Utilisateurs'
        verbose_name_plural = 'Utilisateurs'

    def __str__(self):
        return "id:{}, username:{}".format(self.id, self.username)
