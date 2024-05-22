from django.db import models

# Create your models here.


class UserModel(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'