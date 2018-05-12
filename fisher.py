# _*_ coding:utf-8 _*_

__author__ = 'Xbc'

from app import create_app

app = create_app()


# debug 可以监听代码是否修改过
if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=app.config['DEBUG'], threaded=True)
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)



