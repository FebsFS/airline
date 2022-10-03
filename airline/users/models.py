from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class MyUserManager(BaseUserManager):
   # def _create_user(self, email, username, password, **extra_fields):
    #    if not email:
     #       raise ValueError("Вы не ввели Email")
      #  if not username:
       #     raise ValueError("Вы не ввели имя")
        #user = self.model(
         #   email=self.normalize_email(email),
          #  username=username, **extra_fields)
     #   user.set_password(password)
      #  user.save(using=self._db)
       # return user

    def create_user(self, email, username, password):
        if not email:
          raise ValueError("Вы не ввели Email")
        if not username:
          raise ValueError("Вы не ввели имя")
        user = self.model(
        email=self.normalize_email(email),
        username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        if not email:
               raise ValueError("Вы не ввели Email")
        if not username:
               raise ValueError("Вы не ввели имя")
        user = self.model(
        email=self.normalize_email(email),
        username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email


