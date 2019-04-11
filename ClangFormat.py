#coding:utf-8
#可修改 需要过滤的目录，注意不要和项目主目录同名
Filter_DIRS = ['调试工具', 'HKLib', 'Pods', '.flutter_release', 'Category', 'AppDelegate', 'Request', 'ClassMethods', 'Tool']
#可修改 需要过滤的文件
Filter_FILES = ['AppDelegate.m', 'AppDelegate.h']
import os
import sys
import getopt
path = os.getcwd()

def is_filter_the_dir(path):
	"""
		过滤目录
		"""
	for filter_dir in Filter_DIRS:
		if filter_dir in path:
			return True
	return False

def is_filter_the_file(path):
	"""
	过滤文件
	"""
	name = os.path.basename(path)
	for filter_file in Filter_FILES:
		if name == filter_file:
			return True
	return False

def is_framework(path):
	"""
	framework,第三方框架不需要维护
	"""
	if path.find(".framework")>=0:
		return True
	return False	

for root, dirs, files in os.walk(path):
	if is_filter_the_dir(root):continue
	if is_framework(root):continue
	for name in files:
		if (name.endswith(".h") or name.endswith(".m") or name.endswith(".mm")):
			localpath = root + '/' + name
			if is_filter_the_file(localpath):continue
			print (localpath)
			os.system("clang-format -i %s -style=File" %(localpath))