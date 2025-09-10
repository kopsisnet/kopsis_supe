from django.db import models

class Personel(models.Model):
    ad = models.CharField(max_length=100)
    soyad = models.CharField(max_length=100)
    pozisyon = models.CharField(max_length=100)
    departman = models.CharField(max_length=100, blank=True)
    dogum_tarihi = models.DateField(null=True, blank=True)
    telefon = models.CharField(max_length=20)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.ad} {self.soyad}"
