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
	if not comment_obj.parent_comment:  # 顶级评论
		comment_dic[comment_obj] = OrderedDict()
	else:
		for k in comment_dic:
			if k == comment_obj.parent_comment:  # 找到父评论
				comment_dic[comment_obj.parent_comment][comment_obj] = {}
			else:
				tree_search(comment_dic[k], comment_obj)  # 到下层找


def build_comment_tree(comment_set):
	tree_dic = OrderedDict()
	for comment in comment_set:
		tree_search(tree_dic, comment)
	# return tree_dic.__reversed__()
	return OrderedDict(map(reversed, tree_dic.items()))


def render_comment_tree(comment_tree_dic):
	comment_html_str = ""
	for comment_obj in comment_tree_dic:
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
		if comment_tree_dic.get(comment_obj):  # 如果还有子评论
			ele += render_comment_tree(comment_tree_dic[comment_obj])
		else:
			ele += "</div>"
		ele += "</div>"
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