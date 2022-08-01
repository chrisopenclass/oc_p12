from django.contrib.auth.models import AbstractUser, User, AbstractBaseUser

from django.contrib.auth.models import Group
sales_group, created = Group.objects.get_or_create(name='sales')
support_group, created = Group.objects.get_or_create(name='support')
management_group, created = Group.objects.get_or_create(name='management')


class Users(AbstractUser, AbstractBaseUser):
    User.USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'Utilisateurs'
        verbose_name_plural = 'Utilisateurs'
        ordering = ('first_name',)

    def __str__(self):
        return "id:{}, username:{}".format(self.id, self.username)
