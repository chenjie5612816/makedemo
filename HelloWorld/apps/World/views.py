#coding=utf-8
from uliweb import expose, functions

@expose('/')
def index():
    return '<h1>Hello, Uliweb</h1>'

@expose('/template_Myfirst')
def template_Myfirst():
	return {'content':'Mr ZHAO'}

@expose('/template_Secondly')
def template_Secondly():
	return dict(content = 'Mr jing')

@expose('/template_Thirdly')
def template_Thirdly():
	content = 'MR zhao $ jing' 
	return locals()
