from django.db import models

class Docente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

class Taller(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    cupo = models.IntegerField()
    duracion = models.CharField(max_length=50)
    id_docente = models.ForeignKey(Docente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

class Inscripcion(models.Model):
    id = models.AutoField(primary_key=True)
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    id_taller = models.ForeignKey(Taller, on_delete=models.CASCADE)
    fecha_de_inscripcion = models.DateField()

    def __str__(self):
        return f"{self.id_alumno.nombre} - {self.id_taller.nombre}"
