from django.db import models

# Create your models here.

class AboutPicture(models.Model):
    title = models.CharField(max_length= 255)
    image = models.ImageField(upload_to= 'images/')
    description = models.CharField(max_length= 500)
    # pub_date = models.DateTimeField('pic publish')

    def __str__(self):
        return self.title