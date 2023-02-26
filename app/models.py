from django.db import models

# Create your models here.
class Pengguna(models.Model):
    NamaLengkap = models.CharField(max_length=500)
    EmailPengguna = models.TextField(primary_key=True)
    NoTelp = models.TextField()
