from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, \
                                PermissionsMixin
from django.conf import settings
from django.db.models.deletion import CASCADE


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        #creates a new user and saves
        if not email:
            raise ValueError("User must have email address")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,password, **extra_fields):
        #creates a new superuser and saves
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
        


class User(AbstractBaseUser,PermissionsMixin):

    #custom user model which supports email
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'


class Tag(models.Model):

    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self) :
        return self.name



class Ingredient(models.Model):

    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):

        return self.name

class Recipe(models.Model):

    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE
    )
    duration_mins = models.IntegerField()
    cost = models.DecimalField(max_digits=5,decimal_places=2)
    tags = models.ManyToManyField('Tag')
    Ingredients = models.ManyToManyField('Ingredient') 
    servings = models.IntegerField()
    link = models.CharField(max_length=255,blank=True)

    def __str__(self):

        return self.name


