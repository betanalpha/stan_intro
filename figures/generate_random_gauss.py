import math
import random

for i in range(1000):

  variates=[]

  for j in range (10000): 
    r = random.gauss(0, 1)
    variates.append(r)

  print math.sqrt(reduce(lambda x, y: x + y, [ r * r for r in variates[:1] ]) / 1.0), \
        math.sqrt(reduce(lambda x, y: x + y, [ r * r for r in variates[:10] ]) / 10.0), \
        math.sqrt(reduce(lambda x, y: x + y, [ r * r for r in variates[:100] ]) / 100.0), \
        math.sqrt(reduce(lambda x, y: x + y, [ r * r for r in variates[:1000] ]) / 1000.0), \
        math.sqrt(reduce(lambda x, y: x + y, [ r * r for r in variates[:10000] ]) / 10000.0)
