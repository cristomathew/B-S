from django.db import models
from datetime import datetime
class inquiry(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateField(default=datetime.now)
    user_id = models.IntegerField(blank=True)
    owner_id = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.listing
    