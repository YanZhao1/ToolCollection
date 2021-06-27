from flask import Flask, request, Response, jsonify, abort, redirect, url_for,render_template
from werkzeug.utils import secure_filename  # 文件名安全验证库
import json
import os

# 程序名称
app = Flask(__name__)

# hello word
# get参数获取
@app.route('/')
def hello_world():
    # 获取url链接参数
    info = request.args.get('info')
    print(info)
    return 'Hello World!'


#    return request.args.__str__()

@app.route('/route_test')
def route_test():
    return 'Hello route test!'

# post post参数获取
@app.route('/add', methods=['POST'])
def add():
    print(request.headers)
    print(type(request.json))
    print(request.json)
    result = request.json['a'] + request.json['b']
    return str(result)

#  return json
@app.route('/response_json_test', methods=['POST'])
def response_json_test():
    res = {"aaa": 1, "bbb": 2}
    return jsonify(res)


#    return  Response(json.dumps(res),mimetype='application/json')

# 文件上传目录
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
# 支持的文件格式
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}  # 集合类型
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB


# 判断文件名是否是我们支持的格式
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# 文件上传
@app.route('/upload', methods=['POST'])
def upload():
    upload_file = request.files['image']
    # file_content = request.files['image'].stream.read()
    # 第一次调用f.read()可以读取到内容，这时游标会移动到文章末尾，再次调用f.read()是获取不到内容的，可以使用f.seek(0)将游标移动到文章开头再次调用f.read()即可获取内容
    # 如果你不管第几次调用，不管怎么处理，都无法使用f.read()读取文件内容，我建议你看看你监视里面有没有监视f.read()，
    # 如果有的话每次执行代码的时候都会先执行一次f.read(),所以你代码里当然获取不到内容，移除监视即可

    filename = upload_file.filename
    print("上传的文件的名字是：" + filename)
    print("上传的文件路径是：" + os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
    if upload_file and allowed_file(filename):
        # filename = secure_filename(filename) # secure_filename方法会忽略中文名称如果要用这个函数要提前考虑好中文问题
        # print("上传的文件的名字是："+filename)
        # 将文件保存到 static/uploads 目录，文件名同上传时使用的文件名
        upload_file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
        return 'info is ' + request.form.get('info', '') + '. success'
    else:
        return 'failed'

# 参数url
@app.route('/user/<username>')
def user(username):
    print(username)
    print(type(username))
    return 'hello ' + username

# 参数url
@app.route('/user/<username>/friends')
def user_friends(username):
    print(username)
    print(type(username))
    return 'hello ' + username + ". They are your friends:aa,bbb,ccc. "

# 分页
@app.route('/page/<int:num>')
def page(num):
    print(num)
    print(type(num))
    return '你取的第' + str(num) + "页的数据"

# 分页
@app.route('/page/<int:num1>-<int:num2>')
def page1(num1, num2):
    print(num1)
    print(num2)
    return '你取的第' + str(num1) + "到" + str(num2) + "页的数据"

# 重定向
@app.route('/test1')
def test1():
    print('this is test1')
    return redirect(url_for('hello_world'))

if __name__ == '__main__':
    app.run()
# debug 运行
#   app.run(debug=True)
# 设置参数
#   app.run(host='127.0.0.1', port=5000, debug=True)
