from django.db import models

# Create your models here.
#Create a model for a fairytale
class FairyTale(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()
    land_of_origin = models.CharField(max_length=100)
    similar_tales = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title