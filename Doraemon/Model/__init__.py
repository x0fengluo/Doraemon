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


class Dictate(object):
    """dict可以obj方式访问"""

    def __init__(self, d):
        # since __setattr__ is overridden, self.__dict = d doesn't work
        object.__setattr__(self, '_Dictate__dict', d)

    # Dictionary-like access / updates
    def __getitem__(self, name):
        value = self.__dict[name]
        if isinstance(value, dict):  # recursively view sub-dicts as objects
            value = Dictate(value)
        return value

    def __setitem__(self, name, value):
        self.__dict[name] = value

    def __delitem__(self, name):
        del self.__dict[name]

    # Object-like access / updates
    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        del self[name]

    def __repr__(self):
        return "%s(%r)" % (type(self).__name__, self.__dict)

    def __str__(self):
        return str(self.__dict)



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
            attrs['__tablename__'] = name.lower()

        else:
            attrs['__tablename__'] = getattr(attr_meta, 'table_name')

        mappings = {}  # 保存field
        for attr_name, attr_value in attrs.items():

            if isinstance(attr_value, Field):
                # print('Found maping: %s ==> %s' % (attr_name, attr_value))
                mappings[attr_name] = attr_value

        for k in mappings.keys():
            attrs.pop(k)  # 去除field属性

        # 把所有的Field移到__mappings__里，防止实例的属性覆盖类的同名属性
        attrs['__mappings__'] = mappings

        return type.__new__(mcs, name, bases, attrs)


# 编写基类Model
class Model(with_metaclass(ModelMetaclass)):
    def __init__(self, **kwargs):
        self.dict = {}
        self.dict = Dictate(kwargs)


        self.wrapper = Connect()

        view1 = InsertObserver()
        view2 = UpdateObserver()
        self.wrapper.attach(view1)
        self.wrapper.attach(view2)



    def save(self):
        fields = []
        params = []
        args = []

        for field_name, field in self.__mappings__.items():
            fields.append(field_name)
            args.append(getattr(self.dict, field_name, None))

        print(fields)
        print(args)
        print(self.__tablename__)

        self.wrapper.data = {"key": "val"}
        self.wrapper.status = "insert"

