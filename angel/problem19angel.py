#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
inicio = time.time()

#171

import datetime
count = 0
for y in range(1901,2001):
    for m in range(1,13):
        if datetime.datetime(y,m,1).weekday() == 6:
            count += 1
print (count)



print("Ha tardado {} ms".format((time.time() - inicio) * 1000))