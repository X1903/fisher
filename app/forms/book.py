# _*_ coding:utf-8 _*_
__author__ = 'Xbc'


"""
表单验证
"""

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired  # DataRequired 验证空格,防止用户传入空格


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)