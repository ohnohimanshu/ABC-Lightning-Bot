# chatbot/admin.py
from django.contrib import admin
from .models import Company, Product

admin.site.register(Company)
admin.site.register(Product)
