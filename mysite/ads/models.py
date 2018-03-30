from django.db import models

# Create your models here.

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=100)
    vendor_description = models.CharField(max_length=1000)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')

    def __str__(self):
        return self.vendor_name


class Advertisement(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    advertisement_name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    image_url = models.CharField(max_length=1000)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')
    
    def __str__(self):
        return self.advertisement_name

class Watch(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    number_of_views = models.IntegerField(default=0)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')

    def __str__(self):
        return self.number_of_views