from django.db import models

class Izoh(models.Model):
    ism=models.CharField(max_length=25)
    email=models.EmailField()
    izoh=models.TextField()

    def __str__(self):
        return self.ism



