from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
'''
class AuditEntry(models.Model):
    action = models.CharField(max_length=64)
    username = models.CharField(max_length=200, null=True)

    def __str__(self):
        return '{0} - {1}'.format(self.action, self.username)
    
@receiver(user_logged_in)
def user_logged_in_callback(user, **kwargs):  
    AuditEntry.objects.create(action='user_logged_in', username=user.username)


@receiver(user_logged_out)
def user_logged_out_callback(user, **kwargs):  
    AuditEntry.objects.create(action='user_logged_out', username=user.username)


@receiver(user_login_failed)
def user_login_failed_callback(credentials, **kwargs):
    AuditEntry.objects.create(action='user_login_failed', username=credentials.get('username', None))
'''

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