from django.contrib import admin
from .models import Gundam, Repairs, Weapon

# Register your models here.
admin.site.register(Gundam)
admin.site.register(Repairs)
admin.site.register(Weapon)