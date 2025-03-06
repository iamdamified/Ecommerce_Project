from django.db import models

# Create your models here.

class Hero(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='hero_images')

    class Meta:
        verbose_name_plural = 'Heroes'

    def __str__(self):
        return self.title
    


