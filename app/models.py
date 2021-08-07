from django.db import models

# Create your models here.

class place(models.Model):
    objects = None
    Name = models.CharField(max_length=250)
    Image = models.ImageField(upload_to='PICS')
    Desc = models.TextField()

    def __str__(self):
        return self.Name
