#!/usr/bin/env python
# encoding: utf-8


"""
mail:wqc2008@gmail.com
@createtime: 17/9/28 下午5:19
@license: Apache Licence 2.0
usege:
    ......
    
"""

from random import Random

from Doraemon.Field import *
from Doraemon.Model import Model


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


class Asset(Model):
    """
    资产
    """

    code = StringField(required=True, default=random_str())
    bar_code = StringField(required=True)
    system_mem = IntegerField(required=True, default=1)
    system_disk = IntegerField(required=True, default=100)
    system_core = IntegerField(required=True, default=2)
    outter_ip = StringField(max_length=100, required=True)
    innner_ip = StringField(required=True)

    class Meta:
        table_name = "Asset"





class ServiceCluster(Model):
    """
    服务集群
    """

    parent_id = StringField(required=True)
    name = StringField(required=True)

    class Meta:
        table_name = "ServiceCluster"


class ServiceClusterRole(Model):
    """
    服务集群角色
    """

    service_cluster_id = StringField(required=True)
    role = StringField(required=True)
    port = StringField(required=True)
    config = StringField(required=True)

    class Meta:
        table_name = "ServiceClusterRole"


class ServiceClusterDeploy(Model):
    """
    集群
    """

    group_id = StringField(required=True)
    ServiceCluster_id = StringField(required=True)
    ServiceClusterRole_id = StringField(required=True)
    Asset_id = StringField(required=True)

    class Meta:
        table_name = "cluster"


class Tag(Model):
    """
    标签
    """

    parent_id = StringField(required=True)
    name = StringField(required=True)

    class Meta:
        table_name = "cluster"

#
#
# u = Server()
# u.code = 1
# u.public_ip = 'laowang'
# print(u.save())
