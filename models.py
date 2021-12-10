from django.db import models

# Create your models here.
class Resource(models.Model):
    resource_id = models.AutoField(primary_key=True)
    resouce_link = models.URLField()


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.CharField(max_length=100)
