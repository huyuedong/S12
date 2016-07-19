from django.shortcuts import render, redirect,HttpResponse
from django.conf import settings
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.utils.html import format_html
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from bbs import forms
import re
from base64 import b64encode, b64decode
import os
from django.conf import settings

# Create your views here.
from bbs import models
def root(request):
    return redirect('/bbs')
category_list = models.Category.objects.filter(set_as_top_menu=True).order_by('set_as_top_menu')
def acc_login(request):
    '''
    登录视图
    :param request:
    :return:
    '''
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is not None:
            login(request,user)
            return redirect(request.GET.get('next') or '/bbs')
        else:
            login_err = "用户名或密码错误"
            return render(request,'login.html',{'login_err':login_err})
    return render(request,'login.html')

def acc_logout(request):
    '''
    退出视图
    :param request:
    :return:
    '''
    logout(request)
    return redirect('/bbs')

def index(request):
    '''
    主视图
    :param request:
    :return:
    '''
    category_list = models.Category.objects.filter(set_as_top_menu=True).order_by('set_as_top_menu')
    article_list = models.Article.objects.filter(status='published').order_by('-priority','-pub_date')
    paginator = Paginator(article_list, settings.PER_PAGE)
    page = request.GET.get('page')
    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
         article_list = paginator.page(paginator.num_pages)
    # return render(request,'crm/customers.html',{'customer_list':customer_objs})
    return render(request, 'index.html',{'category_list':category_list,"article_list":article_list})

def category(request,id ):
    '''
    板块视图
    :param request:
    :param id:
    :return:
    '''
    article_list = models.Article.objects.filter(category_id=id,status='published').order_by('-priority','-pub_date')
    paginator = Paginator(article_list, settings.PER_PAGE)
    page = request.GET.get('page')
    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
         article_list = paginator.page(paginator.num_pages)
    return render(request, 'index.html',{'category_list':category_list,"category_id":int(id),"article_list":article_list})



def comment_handler(coment_list):
    '''
    多级回复处理函数
    逻辑有点类似插入排序，定义一个空列表，用来保存处理已经“排序”的回复，遍历回复列表，将回复拆入到合适已经排序好的列表的合适位置
    :param coment_list:
    :return:
    '''
    comment_list_ordered = []
    for coment in coment_list:
        # 遍历评论列表
        if coment.parent_comment is None:
            '''
            如果是根回复，直接追加到已排序列表的后面
            '''
            comment_list_ordered.append((0,coment))
        else:
            parent_comment_index = -1 # 初始化父评论的在列表中的索引值
            for indx in range(len(comment_list_ordered)):
                # 循环评论已排序的列表
                if comment_list_ordered[indx][1].id == coment.parent_comment.id:
                    # 判断是否是父评论
                    parent_comment_index = indx
                    continue
                if comment_list_ordered[indx][1].parent_comment != coment.parent_comment and parent_comment_index!= -1:
                    # 判断是否是父评论的尾部
                    comment_list_ordered.insert(indx, (comment_list_ordered[parent_comment_index][0]+30, coment))
                    break
            else:
                comment_list_ordered.append((comment_list_ordered[parent_comment_index][0]+30, coment))
    return comment_list_ordered



def article_detail(request,article_id):
    '''
    文章详细信息视图，如果是POST请求，说明是给该文章添加评论
    :param request:
    :param article_id:
    :return:
    '''
    article_obj = models.Article.objects.get(id = article_id)
    res = comment_handler(article_obj.comment_set.select_related().filter(comment_type=1).order_by('parent_comment','-id'))
    if request.method == 'POST' and request.user.is_authenticated():
        parent_comment_id = request.POST.get('parent_comment_id')
        comment = request.POST.get('comment')
        new_comment = models.Comment(article_id = article_id,
                                     parent_comment_id = parent_comment_id,
                                     comment_type = 1,
                                     user = request.user.userprofile,
                                     comment = comment)
        new_comment.save()
        return redirect(request.path)
    return render(request,'article.html',{'article':article_obj,"category_list":category_list,"comment_list":res,})


# from random import Random
# def random_str(randomlength=8):
#     str = ''
#     chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
#     length = len(chars) - 1
#     random = Random()
#     for i in range(randomlength):
#         str+=chars[random.randint(0, length)]
#     return str


def get_file_name():
    '''
    生成时间戳类型的文件名函数，避免文件名重复的问题
    :return:
    '''
    import time
    return str(time.time()).replace('.','')

def handle_uploaded_file(f,filename, path=None):
    '''
    上传文章主题图片函数
    :param f: 文件类型的form对象ImageField
    :param filename: 文件名
    :param path: 路径（相对）
    :return:
    '''
    if path is None:
        path = './'
    with open(os.path.join(path, filename), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@login_required(login_url='bbs/login')
def new_article(request):
    '''
    发布文章视图
    :param request:
    :return:
    '''
    import datetime
    if request.method == 'POST':
        next = request.GET.get('next')
        if next is None:
            next = '/bbs'
        form = forms.new_article_form(request.POST,request.FILES) # 创建form对象
        if form.is_valid():
            # 判断是否验证通过
            request_dic = form.clean()
            head_img = request_dic.get('head_img')
            filename= '%s.%s' %(get_file_name(),head_img.name.split('.')[1])
            head_img_str = '%s/%s' %(settings.UPLOADS_PATH,filename)
            handle_uploaded_file(head_img,filename,os.path.join(settings.BASE_DIR, settings.UPLOADS_PATH)) # 保存主题图片
            title = request.POST.get('title')
            brief = request.POST.get('brief')
            category = request_dic.get('category')
            status = request.POST.get('status')
            content = request.POST.get('content')
            res = re.findall(r'src="(data:image/[a-z]+;base64,[^"]+)"',content) # 通过正则表达式获取富文本编辑器里的媒体文件
            for media in res:
                _tmp = media.split(',') # 分离媒体类型等头信息和具体内容
                filename = get_file_name()
                exname = str(re.findall('[\/]([a-z]+);', _tmp[0])[0]) # 通过正则匹配头信息获取文件后缀名
                with open(os.path.join(os.path.join(settings.BASE_DIR, settings.UPLOADS_PATH),'%s.%s' %(filename,exname)), 'wb') as f:
                    f.write(b64decode(_tmp[1])) # 写入文件
                    filename = '%s.%s' %(filename,exname)
                    content = content.replace(media, "/%s/%s" %(settings.UPLOADS_PATH, filename))
            if status == 'published':
                pub_date = datetime.datetime.now()
            else:
                pub_date = None
            new_article = models.Article(title = title,
                                         brief = brief,
                                         category_id = category,
                                         status = status,
                                         content = content,
                                         head_img = head_img_str,
                                         author = request.user.userprofile,
                                         pub_date = pub_date
                                         )
            new_article.save()

        else:
            print('验证失败')
            print(form.errors)
        return redirect(next)
    else:
        form = forms.new_article_form()
    return render(request,'create_article.html',{'form':form,"category_list":category_list})

@login_required(login_url='bbs/login')
def click_thumb(request):
    '''
    点赞视图，通过ajax的post请求
    :param request:
    :return:
    '''
    parent_comment_id = request.POST.get('parent_comment_id')
    article_id = request.POST.get('article_id')
    res = models.Comment.objects.filter(article_id = article_id,
                                        parent_comment_id = parent_comment_id,
                                        comment_type=2,
                                        user=request.user.userprofile).first() # 查询点赞
    if not res: # 同一用户是否已经给文章或评论点过赞
        # 没点过就创建点赞
        new_comment = models.Comment(article_id = article_id,
                                     parent_comment_id = parent_comment_id,
                                     comment_type=2,
                                     user=request.user.userprofile)
        new_comment.save()
        return HttpResponse('add')
    else:
        # 否则删除
        res.delete()
        return HttpResponse('del')
