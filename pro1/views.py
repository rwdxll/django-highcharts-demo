#-*-coding:utf-8-*-

from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	d={'1.htldxhzj.duapp.com': 9398,'gtxapi.cdn.duapp.com': 79496,'www.xxx.com': 2477070,'www.baidu.com': 1465,'www.bing.com': 777,'www.aaa.com': 1113101,'www.ccc.net.cn': 922,'www.zhanimei.ga': 29847,'www.zhanimei.ml': 40155,'www.zhasini.ml': 373436}
	categories = d.keys()
	data = d.values()
	return render_to_response('index.html',{'categories':categories,'data':data})
