from django.db import models


# Create your models here.

class FruitFaq(models.Model):
    image_url = models.CharField(max_length=150)
    fruit = models.CharField(max_length=150)
    fruit_faq = models.CharField(max_length=500)

    def __str__(self):
        return self.fruit
