from django.contrib import admin
from .models import tecnico,orden,cliente

# Register your models here.


admin.site.register(tecnico)
admin.site.register(cliente)
admin.site.register(orden)