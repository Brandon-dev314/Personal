from django.db import models

class Project8(models.Model):
    title = models.CharField(max_length=200, verbose_name= "Titulo")
    description=models.TextField(verbose_name= "Descripción")
    image=models.ImageField(upload_to= "projects",verbose_name= "Imagen")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacíón")
    updated=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title

