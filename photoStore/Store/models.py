from django.db import models

class photo(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    photo_url = models.CharField(max_length=2048)
    
    def __str__(self):
        return self.title


    photo1 = photo()