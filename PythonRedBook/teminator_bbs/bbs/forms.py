import re
from django import forms
from django.core.exceptions import ValidationError
from bbs import models


class new_article_form(forms.Form):
    '''
    新建文章form，只需要两个字段就好了，其他直接前端完成
    '''
    category = forms.CharField(widget=forms.Select(attrs={'class':'form-control'}))
    head_img = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))

    def __init__(self,*args,**kwargs):
        super(forms.Form, self).__init__(*args,**kwargs)
        self.fields['category'].widget.choices = models.Category.objects.all().order_by('id').values_list('id','name')