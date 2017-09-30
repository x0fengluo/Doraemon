#!/usr/bin/env python
# encoding: utf-8


"""
mail:wqc2008@gmail.com
@createtime: 17/9/28 上午11:51
@license: Apache Licence 2.0
usege:
    ......
    
"""

from bson.objectid import ObjectId, InvalidId


class Field(object):

    def __init__(self, default=None, **args):
        self._fieldname = None
        self.default_value = default

    def _get_fieldname(self):
        return self._fieldname

    def _set_fieldname(self, v):
        self._fieldname = v

    fieldname = property(_get_fieldname, _set_fieldname)

    def get_raw(self, obj):
        return self.__get__(obj)

    def __get__(self, obj, type=None):
        v = getattr(obj, self.get_obj_key(),
                    self.default_value)
        return v

    def __set__(self, obj, value):
        if value is not None:
            setattr(obj, self.get_obj_key(), value)

    def __del__(self):
        pass

    def get_key(self):
        return self.fieldname

    def get_obj_key(self):
        return '_' + self.fieldname


class IntegerField(Field):
    def __init__(self, default=0, **kwargs):
        super(IntegerField, self).__init__(default=default,
                                           **kwargs)

    def __set__(self, obj, value):
        value = float(value)
        super(IntegerField, self).__set__(obj, value)


class StringField(Field):
    def __set__(self, obj, value):
        super(StringField, self).__set__(obj, value)
