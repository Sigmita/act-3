# app_Netflix/admin.py
from django.contrib import admin
from .models import Usuario # Asegúrate de importar tu modelo

admin.site.register(Usuario)