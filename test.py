# -*- coding: utf-8 -*-
# @Time    : 2020-11-24 10:21
# @Author  : xzr
# @File    : test
# @Software: PyCharm
# @Contact : xzregg@gmail.com
# @Desc    : 

import json
from dataclasses import dataclass

from objectdict import ObjectDict


# @dataclass
class SimpleExamplea(ObjectDict):
    int_field: int  # = 1
    bbb: str  # = 'a'


@dataclass
class SimpleExample:
    int_field: int
    asd: SimpleExamplea


if __name__ == '__main__':
    a = SimpleExamplea()
    a.int_field = 2
    a.bbb = 'b'
    a.__dict__

    print(json.dumps(a), a, a.int_field)
    b = SimpleExamplea(int_field=3, bbb='c')
    print(json.dumps(b), b, b.bbb)
    c = SimpleExamplea()
    c.from_json('{"asd":3,"bbb":4}')
    c.aa = 'oo'
    print(c, c.asd, c.bbb)
