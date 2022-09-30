from django.contrib import admin

#lahat ng idedeclare nating table sa database is ilalagay dito

# Register your models here.
from .models import inventory,message #kailangan iregister yung model para magamit
admin.site.register(inventory)
admin.site.register(message)
# admin.site.register(all_message)