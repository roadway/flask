# coding: utf-8 
from flask import Flask,request,render_template

#解决Python2.7的UnicodeEncodeError: ‘ascii’ codec can’t encode异常错误
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
lib_path = "/home/pi/mysite/flask/lib/"
sys.path.append(lib_path)
#从模块test_class引入类People
from test_class import People
#创建数据访问类的实例
mybaby=People('落雨天',10)
mn='mybaby%s' % mybaby.name

app = Flask(__name__) 
@app.route('/') 
def index(): 
	return render_template('index.html',name=mybaby.name)
if __name__ == '__main__': 
	app.run()
