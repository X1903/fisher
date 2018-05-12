
from flask import current_app, flash, redirect, url_for
from flask_login import login_required, current_user   # 代表当前访问网站的用户

from app.models.base import db
from app.models.gift import Gift
from . import web


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'ok'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    '''怎送此书'''
    if current_user.can_save_to_list(isbn):
        #  事物
        # rollback
        # try:
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id   # current_user代表实例化后的User模型
            ##############
            current_user.beans += current_app.config['BEANS_UPLODA_ONE_BOOK']
            db.session.add(gift)

            # db.session.commit()
        # except Exception as e:
        #     db.session.rollback()
        #     raise e
    else:
        flash('这本书已经添加到你的赠送清单或已存在你的心愿清单, 请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



