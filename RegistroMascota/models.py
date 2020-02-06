from django.db import models

# Create your models here.

class Raza(models.Model):
    nombre= models.CharField(max_length=20)


    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    nombre = models.CharField(max_length=20)

    raza = models.ForeignKey('Raza', on_delete=models.CASCADE, db_column="fk_raza")


    foto= models.ImageField(upload_to="photo_mascota", null=True)

    def __str__(self):
        return self.nombre

