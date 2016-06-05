from django.contrib import admin
from app01 import models
# Register your models here.


# 自定义动作
def make_forbidden(modelAdmin, request, queryset):
	queryset.update(status="forbidden")
# 设置在前端显示的动作名
make_forbidden.short_description = "设为禁书"


# 定制book的Django admin管理
class BookAdmin(admin.ModelAdmin):
	# 定义要在admin界面显示的字段,注意list_display默认是不能显示many_to_many字段的。
	list_display = ["id", "title", "publisher", "publication_Date", "colored_status"]
	# 按什么排序
	ordering = ["publication_Date", ]
	# 定义搜索框
	search_fields = ["title", "publisher__name"]  # 两个下划线表示跨表操作（查询）
	# 设置过滤条件
	list_filter = ["publisher", "publication_Date"]
	# 是否可以在页面直接修改。
	# admin默认第一个字段是链接，链接字段默认无法修改。
	list_editable = ["title", "publication_Date"]
	# 每页显示的记录条数
	list_per_page = 10
	# 记录编辑页面配置多对多的筛选（原来下拉选择框改为横向选择框）
	filter_horizontal = ["authors", ]  # 多对多
	# 记录编辑页面外键筛选（原来下拉选择框改为横向选择框）
	raw_id_fields = ["publisher", ]  # 外键
	# 自定义动作
	actions = [make_forbidden, ]

# 将定制的model admin和model一起注册
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Author)
admin.site.register(models.Publisher)

