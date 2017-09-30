#!/usr/bin/env python
# encoding: utf-8


"""
mail:wqc2008@gmail.com
@createtime: 17/9/28 下午5:19
@license: Apache Licence 2.0
usege:
    ......
    
"""



from Doraemon.Field import *
from Doraemon.Model import Model



class User(Model):


    id = IntegerField('id')
    name = StringField('name')

    class Meta:
        table_name ="table_name"

u = User(id=1, name='laowang')
u.save()

