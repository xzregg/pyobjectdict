# -*- coding: utf-8 -*-
# @Time    : 2021-01-06 17:00
# @Author  : xzr
# @File    : test_objectDict
# @Software: PyCharm
# @Contact : xzregg@gmail.com
# @Desc    :
import json
from unittest import TestCase

from objectdict import ObjectDict


class TestObjectDict(TestCase):

    def test_value(self):
        class SimpleObjectDict(ObjectDict):
            int_field = 1
            str_field = 'a'
            dict_field = {}
            int2_f: int

        instance = SimpleObjectDict()
        instance.int_field = 2
        instance.str_field = 'b'
        instance.dict_field = {'3': 4}
        instance.other_filed = 'asda'
        print(instance.int_field)

        self.assertEqual(SimpleObjectDict().int_field, 1)
        self.assertEqual(SimpleObjectDict().str_field, 'a')
        self.assertEqual(SimpleObjectDict().dict_field, {})

        print(SimpleObjectDict(), instance, instance.int_field)

        self.assertEqual(instance.int_field, 2)
        instance['int_field'] = 5
        instance.int2_f = 'basd'
        self.assertEqual(instance.int_field, 5)
        print(SimpleObjectDict({"int_field": 4}, new_field='3'), instance, instance.int_field,
              SimpleObjectDict().from_json(json.dumps(instance)))

        self.assertEqual(SimpleObjectDict(), SimpleObjectDict().from_json(json.dumps(SimpleObjectDict())))

        self.assertEqual(instance.str_field, 'b')
        self.assertEqual(instance.dict_field, {'3': 4})
        self.assertEqual(instance.other_filed, 'asda')

        self.assertEqual(instance, json.loads(json.dumps(instance)))
