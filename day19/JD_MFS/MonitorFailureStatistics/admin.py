from django.contrib import admin
from MonitorFailureStatistics import models

# Register your models here.


class FaultAdmin(admin.ModelAdmin):
	search_fields = ('str_time', 'fault_ip', 'handle_person')
	list_filter = ('notify_person', 'handle_person')
	list_display = ("fault_info", "occ_time", "time_consuming", "colored_status", "notify_person", "handle_person", "date")

admin.site.register(models.Fault, FaultAdmin)
