from django.db import models

# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='titulo')
    tecnology = models.CharField(max_length=100, verbose_name='tecnologia')
    description = models.TextField(verbose_name="Descripción", null=True)
    main_image = models.ImageField(upload_to='imagenes/',verbose_name="imagen",null=True)
    publish = models.BooleanField(default=False)
    
    #este constructor te retorna la informacion en la table del super admin
    def __str__(self):
        return self.title
    