from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    education = models.CharField(max_length=500)
    accomplishments = models.CharField(max_length=1000)
    work_experence = models.CharField(max_length=1000)
    certifications = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name
    
