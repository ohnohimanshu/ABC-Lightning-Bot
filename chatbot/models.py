# chatbot/models.py
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    locations = models.CharField(max_length=200)  # Example: "123 Main St, Cityville; 456 Side St, Townsville"
    business_hours = models.CharField(max_length=200)  # Example: "Mon-Fri: 9 AM - 6 PM, Sat: 10 AM - 4 PM"

    def __str__(self):
        return self.name

class Product(models.Model):
    PRODUCT_TYPE_CHOICES = (
        ('street', 'Solar Powered Street Light'),
        ('driveway', 'Solar Powered Driveway Light'),
        ('wall', 'Solar Powered Outside Wall Light'),
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    specs = models.TextField(help_text="Specifications (e.g., dimensions, battery life, etc.)")
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES)

    def __str__(self):
        return self.name
