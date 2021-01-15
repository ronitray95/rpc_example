#!/usr/bin/env python3

import rpc


rpc.init()
p, msg = rpc.power(5, 33)
print(p)
print(msg)

p, msg = rpc.power(5, 3.4)
print(p)
print(msg)

p, msg = rpc.sqrt(565)
print(p)
print(msg)