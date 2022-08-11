from django.contrib import admin
from .models import Gundam, Repairs, Weapon, Photo

# Register your models here.
admin.site.register(Gundam)
admin.site.register(Repairs)
admin.site.register(Weapon)
admin.site.register(Photo)
