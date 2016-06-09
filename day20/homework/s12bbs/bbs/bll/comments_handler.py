#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
生成层级评论树的模块
"""
from bbs.bll import datetime_handler
from collections import OrderedDict


def tree_search(comment_dic, comment_obj):
	"""
	递归生成评论树
	:param comment_dic: 目标字典
	:param comment_obj: 评论对象
	:return:
	"""
	if not comment_obj.parent_comment:  # 顶级评论
		comment_dic[comment_obj] = OrderedDict()
	else:
		for k in comment_dic:
			if k == comment_obj.parent_comment:  # 找到父评论
				comment_dic[comment_obj.parent_comment][comment_obj] = {}
			else:
				tree_search(comment_dic[k], comment_obj)  # 到下层找


def build_comment_tree(comment_set):
	"""
	将评论按时间先后顺序和父节点生成有序字典
	:param comment_set: 后台返回的评论结果集
	:return:
	"""
	tree_dic = OrderedDict()
	for comment in comment_set:
		tree_search(tree_dic, comment)
	return tree_dic


def render_comment_tree(comment_tree_dic):
	"""
	遍历得到的有序的评论字典渲染生成前端的html
	:param comment_tree_dic:
	:return:
	"""
	comment_html_str = ""
	for comment_obj, son_dic in reversed(comment_tree_dic.items()):  # 按时间先后倒序显示
		ele = '''
			<div class="media">
				<div class="media-left">
					<a href="{0}" class="comment-head-img">
						<img class="media-object comment-head-img" src="{1}" alt="{2}的头像">
					</a>
				</div>
			<div class="media-body">
				<h4 class="media-heading">{2}<small class="margin-left-twenty">{3}</small></h4>
				{4}
		'''.format(
			comment_obj.user.id,
			comment_obj.user.get_head_img(),
			comment_obj.user.name,
			datetime_handler.readable_date(comment_obj.date),
			comment_obj.comment,
		)
		if son_dic:  # 如果还有子评论
			ele += render_comment_tree(son_dic)
		else:  # 结束子评论
			ele += "</div><hr/>"
		ele += "</div>"  # 结束评论
		comment_html_str += ele
	return comment_html_str


'''
<div class="media">
  <div class="media-left">
    <a href="#">
      <img class="media-object" src="..." alt="...">
    </a>
  </div>
  <div class="media-body">
    <h4 class="media-heading">Media heading</h4>
    ...
  </div>
</div>
'''