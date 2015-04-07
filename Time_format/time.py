#!/usr/bin/python

import datetime

a = datetime.datetime(100,1,1,7,00,00) #7:00:00
print a.time()

b = datetime.datetime(100,1,1,7,30,00) #7:30:00
print b.time()

c = datetime.datetime(100,1,1,19,00,00) #19:00:00
print c.time()

d = datetime.datetime(100,1,1,19,30,00) #19:30:00
print d.time()
