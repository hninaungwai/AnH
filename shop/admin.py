from django.contrib import admin
from .models import Pharmacy

# Register your models here.
class PharmacyAdmin(admin.ModelAdmin):
	list_display = ['name', 'batch', 'price', 'promotion', 'foc', 'exp', 'start']
	list_filter = ['batch', 'price', 'exp']
	search_fields = ['name',]

admin.site.register(Pharmacy, PharmacyAdmin)