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
            int_field: int = 1
            str_field = 'a'
            dict_field = {}
            int2_f: int
            _protect = 'protect'

            @classmethod
            def classmethod(cls):
                pass

            @property
            def proty(cls):
                return 'property'

            def asd(self):
                return 'asd'

        self.assertEqual(ObjectDict(), {})

        self.assertEqual(SimpleObjectDict().int_field, 1)
        self.assertEqual(SimpleObjectDict().str_field, 'a')
        self.assertEqual(SimpleObjectDict().dict_field, {})
        self.assertEqual(SimpleObjectDict(), SimpleObjectDict().from_json(json.dumps(SimpleObjectDict())))

        instance = SimpleObjectDict()

        self.assertEqual(SimpleObjectDict().int_field, instance.int_field)

        instance.int_field = 2
        self.assertEqual(instance.int_field, 2)

        instance.str_field = 'b'
        self.assertEqual(instance.str_field, 'b')
        instance.dict_field = {'3': 4}
        instance.other_filed = 'asda'
        self.assertEqual(instance.other_filed, 'asda')

        instance.update({'bb': 3})
        self.assertEqual(instance['bb'], 3)
        instance.update = 3
        self.assertEqual(instance.update, 3)
        self.assertEqual(instance, json.loads(json.dumps(instance)))

        print(ObjectDict(), SimpleObjectDict(), json.dumps(SimpleObjectDict()), instance, instance.int_field)

        instance2 = SimpleObjectDict({"int_field": 4}, new_field='3')

        self.assertEqual(instance2.new_field, '3')
        self.assertEqual(instance2.int_field, 4)
        self.assertEqual(instance2, json.loads(json.dumps(instance2)))

        instance3 = SimpleObjectDict()
        json_data = '{"a":1,"str_field":"b"}'
        instance3.from_json(json_data)
        self.assertEqual(instance3.a, 1)
        self.assertEqual(instance3.str_field, "b")
