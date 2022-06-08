from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=100)
    filledPasswords = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.username} preencheu a senha.'