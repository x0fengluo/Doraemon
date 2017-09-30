#!/usr/bin/env python
# encoding: utf-8


"""
mail:wqc2008@gmail.com
@createtime: 17/9/28 下午12:00
@license: Apache Licence 2.0
usege:
    ......
    
"""



import datetime
from random import Random


from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import *




def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str




class Server(Document):
    """
    资产信息
    """

    code = StringField(unique=True, required=True, default=random_str())
    public_ip = StringField(unique=True, max_length=100, required=True)
    innner_ip = StringField(required=True)
    sever_type = StringField(max_length=3, choices=('KVM', 'Docker', 'Server'))
    system_mem = IntField(required=True, default=1)
    system_disk = IntField(required=True, default=100)
    system_core = IntField(required=True, default=2)

    ext_ip = ListField(EmbeddedDocumentField('ServerCluster'), required=False)
    data_disk = ListField(EmbeddedDocumentField('DataDisk'), required=False)

    create_time = DateTimeField(default=datetime.datetime.now, required=True)


class service(Document):
    """
    资产信息
    """

    name = StringField(unique=True, required=True)
    port = StringField(unique=True, max_length=100, required=True)
    role = StringField(required=True)
    group = StringField(unique=True, max_length=100, required=True)



class Tag(Document):

    name = StringField(required=True)
    parent_id = StringField(required=True)



class ServerCluster(Document):

    name = StringField(required=True)



class BusinessCluster(EmbeddedDocument):

    StringField(required=True)





