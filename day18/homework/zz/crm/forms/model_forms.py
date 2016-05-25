#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

from crm import models
from django.forms import ModelForm


class UserProfileForm(ModelForm):
	class Meta:
		model = models.UserProfile
		fields = "__all__"


class SchoolForm(ModelForm):
	class Meta:
		model = models.School
		fields = "__all__"


class CourseForm(ModelForm):
	class Meta:
		model = models.Course
		fields = "__all__"


class ClassListForm(ModelForm):
	class Meta:
		model = models.ClassList
		fields = "__all__"


class CustomerForm(ModelForm):
	class Meta:
		model = models.Customer
		fields = "__all__"


class ConsultRecordForm(ModelForm):
	class Meta:
		model = models.ConsultRecord
		fields = "__all__"


class CourseRecordForm(ModelForm):
	class Meta:
		model = models.CourseRecord
		fields = "__all__"


class StudyRecordForm(ModelForm):
	class Meta:
		model = models.StudyRecord
		fields = "__all__"


class PaymentRecordForm(ModelForm):
	class Meta:
		model = models.PaymentRecord
		fields = "__all__"
