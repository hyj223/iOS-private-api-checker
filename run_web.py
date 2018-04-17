#coding=utf-8
'''
Created on 2015年11月05日
iOS private api检查 Web启动入口
@author: atool
'''


from app import app
from datetime import timedelta

# 设置静态文件缓存过期时间
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
app.send_file_max_age_default = timedelta(seconds=1)

# 设置Session过期时间
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=1)
# app.permanent_session_lifetime = timedelta(seconds=1)

if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug = True,  threaded = True)