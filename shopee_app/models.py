from django.db import models

# Create your models here.

class SellerDetails_Model(models.Model):
    URL = models.CharField(max_length=100, null=False, default=None)

class GetLinks_Model(models.Model):
    URL = models.CharField(max_length=100, null=False, default=None)
