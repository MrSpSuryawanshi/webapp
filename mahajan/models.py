from django.db import models

# Create your models here.
class bottle(models.Model):
    Name = models.CharField(max_length = 200)
    Last = models.CharField(max_length = 500)
 

    def __str__(self):
        return self.Name
