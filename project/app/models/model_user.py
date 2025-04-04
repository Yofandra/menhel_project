from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class MyUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The username field must be set')
        if not password:
            raise ValueError('The password field must be set')  

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User')
    ]
    username = models.CharField(max_length=50, unique=True, db_index=True)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, null=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username



