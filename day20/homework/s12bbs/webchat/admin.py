from django.contrib import admin
from webchat import models

# Register your models here.


@admin.register(models.WebGroup)
class WebGroupAdmin(admin.ModelAdmin):
	# list_display = ()
	exclude = ()
