#!/usr/bin/env python3

"""
$ find ns0
ns0
ns0/ns1
ns0/ns1/y.py
ns0/ns1/ns2
ns0/ns1/ns2/z.py
ns0/x.py
"""

import ns0.x
import ns0.ns1.y
import ns0.ns1.ns2.z

if __name__ == "__main__":
    assert ns0.x.level == 0
    assert ns0.ns1.y.level == 1
    assert ns0.ns1.ns2.z.level == 2

    assert ns0.ns1.y.x is ns0.x

    assert ns0.ns1.ns2.z.y is ns0.ns1.y
    assert ns0.ns1.ns2.z.x is ns0.x
