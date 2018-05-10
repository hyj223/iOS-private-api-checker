#coding=utf-8
'''
Created on 2015年6月16日

@author: atool
'''
from app import app
from app.utils import StringUtil, PathUtil, OtherUtil, EGKReviewResultUtil
import flask
from flask.globals import request
from werkzeug.utils import secure_filename
import os, shutil
import iOS_private

@app.route('/', methods=['GET'])
def index_page():
    return flask.render_template('main/index_page.html')

allow_ext = ['ipa']
#ipa上传
@app.route('/ipa_post', methods=['POST'])
def ipa_post():
    rst = {}
    pid = StringUtil.get_unique_str()
    ipa_path = None
    try:
        upload_file = request.files['file']
        fname = secure_filename(upload_file.filename)
        suffix_name = fname.split('.')[-1] #以.分隔最后的字符串
        #文件后缀名不对时，不做存储处理
        if not suffix_name in allow_ext:
            rst['success'] = 0
            rst['message'] = 'file ext is not allowed'
        else:
            #为图片名称添加时间戳，防止不同文件同名
            fname = pid + '.' + suffix_name
            ipa_path = os.path.join(PathUtil.upload_dir(), fname) #路径拼接
            upload_file.save(ipa_path) #保存上传的文件
            #获得ipa信息
            rsts = iOS_private.check_app_info_and_provision(ipa_path)
            for key in rsts.keys():
                rst[key] = rsts[key]
            #检查ios私有api
            app = iOS_private.get_executable_path(ipa_path, pid)
            print 'app', app
            methods_in_app, methods_not_in_app, private = iOS_private.check_private_api(app, pid)
            rst['methods_in_app'] = methods_in_app
            rst['private_framework'] = list(private)
            #检查ipa 64支持情况
            arcs = iOS_private.check_architectures(app)
            rst['arcs'] = arcs
            #包文件大小
            ipa_filesize = StringUtil.file_size(ipa_path)
            rst['ipa_filesize'] = str(ipa_filesize)
            #解读数据，审核结果分析
            reviewResult = EGKReviewResultUtil.handleReviewResult(rst)
            reviewResult['success'] = 1
            reviewResult['message'] = '检查成功，数据处理完成'
            rst = reviewResult

    except Exception, e:
        print e
        rst['success'] = 0
        rst['message'] = '检查失败，也许上传的包并非真正的ipa，或者系统出现错误！'
    
    if ipa_path and os.path.exists(ipa_path):
        os.remove(ipa_path) #删除上传的包

    cur_dir = os.getcwd() #删除检查临时目录
    dest_tmp = os.path.join(cur_dir, 'tmp/' + pid)
    if os.path.exists(dest_tmp):
        shutil.rmtree(dest_tmp)
    return OtherUtil.object_2_dict(rst)

#定义404页面
@app.errorhandler(404)
def page_not_found(error):
    return '404'

@app.errorhandler(502)
def server_502_error(error):
    return '502'

@app.route('/not_allow', methods=['GET'])
def deny(error):
    return 'You IP address is not in white list...'