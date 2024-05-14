from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

#-----------------------------------------------------------
#2. A07:2021-Identification and Authentication Failures. Unsafe way.
#3. A02:2021-Cryptographic Failures. Unsafe way.
# Model so that passwords can be saved as plaintext
class UnsafeUser(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username
#-----------------------------------------------------------