from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class StudentManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Students must have a username')
        student = self.model(username=username)
        student.set_password(password)
        student.save(using=self._db)
        return student

class Student(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    
    objects = StudentManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username