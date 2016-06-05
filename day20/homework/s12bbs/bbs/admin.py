from django.contrib import admin

# Register your models here.

from bbs import models


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'author', 'pub_date', 'last_modify', 'status', 'priority')


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('article', 'parent_comment', 'comment_type', 'comment', 'user', 'date')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'set_as_top_menu', 'position_index')


admin.site.register(models.UserProfile)
