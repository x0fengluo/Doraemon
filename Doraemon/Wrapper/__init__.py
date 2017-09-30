#!/usr/bin/env python
# encoding: utf-8


"""
mail:wqc2008@gmail.com
@createtime: 17/9/30 下午2:25
@license: Apache Licence 2.0
usege:
    ......
    
"""

# !/usr/bin/env python
# encoding: utf-8


"""
mail:wqc2008@gmail.com
@createtime: 17/9/29 下午3:39
@license: Apache Licence 2.0
usege:
    ......

"""

from pymongo import uri_parser
from pymongo import MongoClient, ASCENDING, DESCENDING
from pymongo.errors import ConnectionFailure, InvalidURI
from pymongo import InsertOne, DeleteMany, ReplaceOne, UpdateOne

status = ['insert', 'update', 'delete']


class StatusError(BaseException):
    pass


class Subject(object):
    """观察者模式"""

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Connect(Subject):
    def __init__(self, name='Connect'):
        Subject.__init__(self)
        self.name = name
        self._status = 0

        uri = 'mongodb://localhost:27017/udo'
        if uri.startswith("mongodb://"):

            params = uri_parser.parse_uri(uri)

            self.conn = MongoClient(uri)

            self.database = self.conn[params['database']]
        else:
            idx = uri.find("://")
            raise InvalidURI("Invalid URI scheme: "
                             "%s" % (uri[:idx],))

        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):

        if value not in status:
            raise StatusError("status should use ['insert','update','delete']")
        self._status = value

        self.notify()


class InsertObserver(object):
    def update(self, subject):
        # print(subject.conn)
        # print(subject.data)
        # print(subject.status)
        # print(subject.name)

        if subject.status == 'insert':
            subject.database['tabeltest'].insert_one(subject.data)


class UpdateObserver(object):
    def update(self, subject):
        print(subject.conn)
        print(subject.data)
        print(subject.status)
        print(subject.name)


def main():
    data1 = Connect()

    view1 = InsertObserver()
    view2 = UpdateObserver()
    data1.attach(view1)
    data1.attach(view2)

    data1.data = {"key": "val"}
    data1.status = "insert"

    #
    # if __name__ == '__main__':
    #     main()
