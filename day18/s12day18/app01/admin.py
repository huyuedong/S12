from django.contrib import admin

# Register your models here.
from app01 import models


def make_forbidden(modelAdmin, request, queryset):
	queryset.update(status="forbidden")
make_forbidden.short_description = "设为禁书"


# 定制book的Django admin管理
class BookAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "publisher", "publication_Date", "colored_status")
	search_fields = ("title", "publisher__name")
	list_filter = ("publisher", "publication_Date")
	list_editable = ("title", "publication_Date")
	list_per_page = 10
	filter_horizontal = ("authors", )  # 多对多
	raw_id_fields = ("publisher", )  # 外键
	actions = [make_forbidden, ]

admin.site.register(models.Author)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Publisher)
