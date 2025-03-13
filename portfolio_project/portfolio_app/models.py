from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=250)
    link=models.CharField(max_length=100, null=True, blank=True)
    gitlink=models.CharField(max_length=100, null=True)
    image = models.FileField(upload_to="projects/", blank=True)
    
    def __str__(self):
        return self.title
