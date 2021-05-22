from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    
    def create_user(self, username, email=None, password=None, **extrafields):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username, email=self.normalize_email(email), **extrafields)
        user.set_password(password)
        print(password)
        print(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, username, password, email=None):
        user = self.create_user(username, email, password)
        user.is_staff  = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    favourites = models.CharField(max_length=200,default='')
    rate_listing = models.CharField(max_length=200,default='')
    phone = models.BigIntegerField(default=0, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'