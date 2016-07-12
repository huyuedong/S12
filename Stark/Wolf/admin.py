from django.contrib import admin

# Register your models here.
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from Wolf import models


class UserCreationForm(forms.ModelForm):
	"""
	一个用于创建新用户的表，包含所有需要的字段
	密码和确认密码
	"""

	password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

	class Meta:
		model = models.UserProfile
		fields = ("email", "name", "is_active", "is_admin")

	def clean_password2(self):
		# 检测两次输入的密码是否相同
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(u"两次输入的密码不同。")
		return password2

	def save(self, commit=True):
		# 将密码加密后保存
		user = super(UserCreationForm, self).save(commit=True)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user


class UserChangeForm(forms.ModelForm):
	"""
	修改用户信息的表格
	包括所有的字段，但是密码字段要用加密后的字段代替
	"""
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = models.UserProfile
		fields = ("email", "password", "name", "is_active", "is_admin")

	def clean_password(self):
		"""
		返回初始值
		"""
		return self.initial["password"]


class UserAdmin(BaseUserAdmin):
	"""
	自定义用户管理
	"""
	# 添加和修改用户实例的表
	form = UserChangeForm  # 修改
	add_form = UserCreationForm  # 添加

	# 这些字段用在显示在用户的model
	# 这些字段复写base UserAdmin中在auth.User中指定的字段
	list_display = ("email", "name", "is_admin")
	list_filter = ("is_admin", )
	fieldsets = (
		(None, {"fields": ("email", "password")}),
		("Personal info", {"fields": ("name", )}),
		("Permissions", {"fields": ("is_admin", )}),
	)
	# add_fieldsets不是标准ModelAdmin属性
	# 当创建用户的时候UserAdmin使用下列字段复写get_fieldsets
	add_fieldsets = (
		(None, {
			"classes": ("wide", ),
			"fields": ("email", "name", "password1", "password2")
			}
		),
	)
	search_fields = ("email", )  # 用于检索的字段
	ordering = ("email", )  # 用于排序的字段
	filter_horizontal = ()

# 注册新的UserAdmin
admin.site.register(models.UserProfile, UserAdmin)
# 因为我们不再使用Django内置的权限管理，所以我们就移除注册admin的Group
admin.site.unregister(Group)




