from django.contrib import admin

# Register your models here.

from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
from bbs import models


class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'author', 'pub_date', 'last_modify', 'status', 'priority')


class CommentAdmin(admin.ModelAdmin):
	list_display = ('article', 'parent_comment', 'comment_type', 'comment', 'user', 'date')


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'set_as_top_menu', 'position_index')

admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.UserProfile)

# app_models = apps.get_app_config("bbs").get_models()
# for model in app_models:
# 	try:
# 		modelAdmin = getattr(admin, "{}Admin".format(model))
# 		admin.site.register(model, modelAdmin)
# 	except AttributeError:
# 		pass
# 	except AttributeError:
# 		pass
# 	try:
# 		admin.site.register(model, modelAdmin)
# 	except AlreadyRegistered:
# 		pass
