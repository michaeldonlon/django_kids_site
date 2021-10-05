# customuser/models.py

from django import forms
from django.db import models
from django.contrib import auth
from django.contrib.auth.models import (
        AbstractBaseUser, 
        BaseUserManager, 
        Group,
        Permission
)
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _



class MyUserManager(BaseUserManager):


    def create_user(self, email, first_name, last_name, password=None):
        
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.is_active = False
        user.is_admin = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):

        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        return user


def _user_has_perm(user, perm, obj):
    for backend in auth.get_backends():
        if not hasattr(backend, 'has_perm'):
            continue
        try:
            if backend.has_perm(user, perm, obj):
                return True
        except PermissionDenied:
            return False
    return False

def _user_has_module_perms(user, app_label):
    for backend in auth.get_backends():
        if not hasattr(backend, 'has_module_perms'):
            continue
        try:
            if backend.has_module_perms(user, app_label):
                return True
        except PermissionDenied:
            return False
    return False


class MyCustomUser(AbstractBaseUser):


    class Meta:
        permissions = [
            ('confirmed_user', 'can visit the website'),
        ]


    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        error_messages={
            'unique': ("This email is already in use, please log in or reset your password."),
        },
    )
    first_name = models.CharField(max_length=63, unique=False)
    last_name = models.CharField(max_length=63, unique=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="user_set",
        related_query_name="customuser",
    )
    objects = MyUserManager()
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="user_set",
        related_query_name="user",
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_admin:
            return True
        return _user_has_perm(self, perm, obj)

    def has_perms(self, perm_list, obj=None):
        return all(self.has_perm(perm, obj) for perm in perm_list)

    def has_module_perms(self, app_label):
        if self.is_active and self.is_admin:
            return True
        return _user_has_module_perms(self, app_label)

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin


