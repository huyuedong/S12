from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

# Register your models here.

models_list = apps.get_app_config("crm").get_models()
print(models_list)

for model in models_list:
	try:
		admin.site.register(model)
	except AlreadyRegistered:
		pass
