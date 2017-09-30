#!/usr/bin/env python
# encoding: utf-8


"""
mail:wqc2008@gmail.com
@createtime: 17/9/25 下午3:33
@license: Apache Licence 2.0
usege:
    ......
    
"""

from Doraemon.Field import *
from Doraemon.Wrapper import *
from six import with_metaclass


# 编写ModelMetaclass元类
class ModelMetaclass(type):
    """
    __new__(cls, name, bases, attrs)

    cls: 将要创建的类，类似与self，但是self指向的是instance，而这里cls指向的是class

    name: 类的名字，也就是我们通常用类名.__name__获取的。

    bases: 基类

    attrs: 属性的dict。dict的内容可以是变量(类属性），也可以是函数（类方法）。

    """

    def __new__(mcs, name, bases, attrs):

        if name == 'Model':
            return type.__new__(mcs, name, bases, attrs)
        # print('Found model: %s' % name)


        # 从参数 attrs 中获取 Meta 属性
        attr_meta = attrs.pop('Meta', None)

        if getattr(attr_meta, 'table_name', None) is None:
            attrs['table_name'] = name.lower()

        else:
            attrs['table_name'] = getattr(attr_meta, 'table_name')

        mappings = {}  # 保存field
        for attr_name, attr_value in attrs.items():

            if isinstance(attr_value, Field):
                # print('Found maping: %s ==> %s' % (attr_name, attr_value))
                mappings[attr_name] = attr_value

        for k in mappings.keys():
            attrs.pop(k)  # 去除field属性

        return type.__new__(mcs, name, bases, attrs)


# 编写基类Model
class Model(with_metaclass(ModelMetaclass)):
    def __init__(self, **kwargs):
        self.dict = {}
        self.dict = kwargs

        self.wrapper = Connect()

        o_insert = InsertObserver()
        o_update = UpdateObserver()
        self.wrapper.attach(o_insert)
        self.wrapper.attach(o_update)

    def save(self):
        self.wrapper.table = self.table_name
        self.wrapper.data = self.dict
        self.wrapper.status = "insert"

        return  self.wrapper.insertid
