
from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash   # 用于密码加密
from flask_login import login_user

from app.forms.auth import RegisterForm, LoginForm
from app.models.base import db
from app.models.user import User
from . import web

__author__ = '七月'


@web.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            # user.nickname = form.nickname.data
            # user.email = form.email.data
            user.set_attrs(form.data)  # form.data 包含了所有客户端提交过来的信息
            # user.password = generate_password_hash(form.password.data)   # 写入模型里面了
            db.session.add(user)
        # db.session.commit()

        return redirect(url_for('web.login'))  # 注册成功重定向到登录页面


    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=True)   # remember=True  默认保存365天
            next = request.args.get('next')  # args 获取URL ?后的数据
            if not next or not next.startswith('/'):   # 防止重定向攻击
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账户不存在或密码错误')
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
