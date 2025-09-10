from django.db import models

class Personel(models.Model):
    ad = models.CharField(max_length=100)
    soyad = models.CharField(max_length=100)
    pozisyon = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    email = models.EmailField()
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.ad} {self.soyad}"
