#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
保库的题：
*第 0000 题：
**将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
此题目 需要的引入多个模块 PIL
"""
from PIL import Image, ImageDraw, ImageFont


class AddNumToImage(object):
	def __init__(self):
		self._font = None
		self._image = None

	def open(self, path):
		"""
		打开图片
		:param path: 图片路径
		:return:
		"""
		self._image = Image.open(path)
		return True

	def setFont(self, font_path, size):
		"""
		对要添加的文本设置字体路径和字体大小
		:param font_path: 本地字体路径
		:param size: 字体大小
		:return:
		"""
		self._font = ImageFont.truetype(font_path, size)
		return True

	def draw_str(self, position, str, colour='#ff0000',):
		"""
		绘制
		:param position: 添加文本的坐标
		:param str: 添加文本的内容
		:param colour: 添加文本的颜色
		:return:
		"""
		draw = ImageDraw.Draw(self._image)
		draw.text(position, str, font=self._font, fill=colour)
		self._image.show()
		self._image.save('result.jpg', 'jpeg')
		return True


if __name__ == "__main__":
	a = AddNumToImage()
	a.open("E:\\test.jpg")
	a.setFont("C:\\Windoes\\Fonts\\arial.ttf", 20)
	a.draw_str((110, 3), "7")
