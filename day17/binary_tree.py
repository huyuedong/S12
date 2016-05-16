#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com


class TreeNode(object):
	def __init__(self, data=0, left=0, right=0):
		self.data = data
		self.left = left
		self.right = right


class BTree(object):
	def __init__(self, root=0):
		self.root = root

	def preOrder(self, treenode):
		"""
		先根节点，再左节点，再右节点
		:param treenode:
		:return:
		"""
		if treenode is 0:
			return
		print(treenode.data)
		self.preOrder(treenode.left)
		self.preOrder(treenode.right)

	def inOrder(self, treenode):
		"""
		先左节点，再根节点，再右节点
		:param treenode:
		:return:
		"""
		if treenode is 0:
			return
		self.inOrder(treenode.left)
		print(treenode.data)
		self.inOrder(treenode.right)

	def postOrder(self, treenode):
		"""
		先左节点，再右节点，再根节点
		:param treenode:
		:return:
		"""
		if treenode is 0:
			return
		self.postOrder(treenode.left)
		self.postOrder(treenode.right)
		print(treenode.data)
