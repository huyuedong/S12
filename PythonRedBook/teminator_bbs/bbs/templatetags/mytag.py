from django import template
from django.utils.html import format_html
from bbs import models
register = template.Library()


@register.simple_tag
def filter_comment(article_obj):
    '''
    用来统计文章有多少评论、多少赞
    '''
    query_set = article_obj.comment_set.select_related()
    comments = {
        'comment_count': query_set.filter(comment_type=1).count(),
        'thumb_count': query_set.filter(comment_type=2).count(),
    }
    return comments

@register.simple_tag
def filter_comment_comment(article_obj):
    '''
    用来统计评论有多少子评论、多少赞
    '''
    query_set = article_obj.my_children.all()
    comments = {
        'comment_count': query_set.filter(comment_type=1).count(),
        'thumb_count': query_set.filter(comment_type=2).count(),
    }
    return comments
@register.simple_tag
def get_thumb(obj, user):
    '''
    用来判断是否给文章或评论点过赞，如果点过赞返回的是一个class样式thumbed
    '''
    if isinstance(obj, models.Article):
        # 判断是否是文章
        parent_comment_id = None
        article_id = obj.id
    elif isinstance(obj, models.Comment):
        # 判断是否是评论
        article_id = obj.article.id
        parent_comment_id = obj.id
    else:
        return ''
    comment_obj = models.Comment.objects.filter(article_id = article_id, parent_comment_id = parent_comment_id, comment_type=2, user=user.userprofile)
    if comment_obj:
        return 'thumbed'
    else:
        return ''

@register.simple_tag
def guess_page(current_page,loop_num):
    '''
    分页过滤标签
    '''
    offset = abs(current_page - loop_num)
    if offset <3:
        if current_page == loop_num:
            page_ele = '''<li class="active"><a href="?page=%s">%s</a></li>''' %(loop_num,loop_num)
        else:
            page_ele = '''<li class=""><a href="?page=%s">%s</a></li>''' %(loop_num,loop_num)
        return format_html(page_ele)
    else:
        return ''