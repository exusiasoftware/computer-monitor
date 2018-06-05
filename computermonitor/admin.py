from django.contrib import admin
from .models import Computer, ComputerBackup

admin.site.register(Computer)
admin.site.register(ComputerBackup)