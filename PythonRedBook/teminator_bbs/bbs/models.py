from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime
from django.conf import settings
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 255,
                             verbose_name = '标题')
    brief = models.CharField(null = True,
                             blank = True,
                             max_length = 255,
                             verbose_name = '简介')
    category = models.ForeignKey("Category",
                                 verbose_name = '板块')
    content = models.TextField(verbose_name = '正文')
    head_img = models.ImageField( upload_to = settings.UPLOADS_PATH,
                                  verbose_name='主题图片')
    author = models.ForeignKey("UserProfile" ,
                               verbose_name = '作者')
    pub_date = models.DateTimeField(blank = True,
                                    null = True ,
                                    verbose_name = '发布时间')
    last_modify = models.DateTimeField(auto_now = True ,
                                       verbose_name='最后修改时间')
    priority = models.IntegerField(default=1000,
                                   verbose_name = '优先级')
    status_choices = settings.STATUS_CHOICES
    status = models.CharField(choices = status_choices,
                              default = 'published',
                              max_length = 32,
                              verbose_name = '状态')
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '文章列表'
        verbose_name_plural = verbose_name
    def clean(self):
        if self.status == 'draft' and self.pub_date is not None:
            raise ValidationError(('Draft entries may not have a publication date.'))
        if self.status == 'published' and self.pub_date is None:
            self.pub_date = datetime.date.today()

class Comment(models.Model):
    article = models.ForeignKey(Article,verbose_name=u"所属文章")
    parent_comment = models.ForeignKey('self',
                                       related_name = 'my_children',
                                       blank = True,
                                       null = True,
                                       verbose_name = '上一级评论')
    comment_choices = settings.COMMENT_CHOICES
    comment_type = models.IntegerField(choices = comment_choices,
                                       default = 1,
                                       verbose_name = '类型')
    user = models.ForeignKey("UserProfile", verbose_name='评论者')
    comment = models.TextField(blank = True,
                               null = True,
                               verbose_name = '正文')
    date = models.DateTimeField(auto_now_add=True, verbose_name='时间')

    def clean(self):
        if self.comment_type == 1 and self.comment is None:
            raise ValidationError(u'评论内容不能为空，sb')
    def __unicode__(self):
        return "%s,%s" %(self.article,self.comment)
    def __str__(self):
        return "%s,%s" %(self.article,self.comment)
    class Meta:
        verbose_name = '评论列表'
        verbose_name_plural = verbose_name

class Category(models.Model):
    name = models.CharField(max_length = 64,
                            unique = True,
                            verbose_name='板块名')
    brief = models.CharField(null = True,
                             blank = True,
                             max_length = 255,
                             verbose_name = '')
    set_as_top_menu = models.BooleanField(default=False)
    position_index = models.SmallIntegerField()
    admins = models.ManyToManyField("UserProfile",blank=True)

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length = 32)
    signature= models.CharField(max_length = 255,
                                blank = True,
                                null = True)
    head_img = models.ImageField(blank = True,
                                 null = True,
                                 upload_to = settings.UPLOADS_PATH)
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name