#!/usr/bin/env python
# encoding: utf-8


"""
mail:wqc2008@gmail.com
@createtime: 17/9/25 下午3:47
@license: Apache Licence 2.0
usege:
    ......
    
"""

import unittest

from mongoengine import connect

from Doraemon.Model import  Server, DataDisk


class demoTest(unittest.TestCase):

    def setUp(self):

        connect(host='mongodb://localhost/test')

    def test_save(self):

        return

        data_disk = DataDisk()

        server = Server(public_ip ="115.115.115.118", innner_ip="10.0.0.115", data_disk = [data_disk])
        server.save()


    def test_find(self):

        return
        for user in Server.objects.filter(public_ip ="115.115.115.118"):
            print (user.public_ip)

    def test_mongodb_execl(self):

        from openpyxl import Workbook
        from openpyxl.chart import (
            AreaChart,
            Reference,
        )

        wb = Workbook()
        ws = wb.active
        ws.title = 'testSheet'


        rows = [
            ['Number', 'Batch 1', 'Batch 2'],
            [2, 40, 30],
            [3, 40, 25],
            [4, 50, 30],
            [5, 30, 10],
            [6, 25, 5],
            [7, 50, 10],
        ]

        for row in rows:
            ws.append(row)

        chart = AreaChart()
        chart.title = "Area Chart"
        chart.style = 13
        chart.x_axis.title = 'Test'
        chart.y_axis.title = 'Percentage'

        cats = Reference(ws, min_col=1, min_row=1, max_row=7)
        data = Reference(ws, min_col=2, min_row=1, max_col=3, max_row=7)
        chart.add_data(data, titles_from_data=True)
        chart.set_categories(cats)

        ws.add_chart(chart, "A10")

        wb.save("area.xlsx")


if __name__ == '__main__':
    unittest.main()
