mul= lambda x,y: x*y
print(mul(7,10))

from functools import reduce

scores = [75, 65, 80, 95, 50]

total = reduce(lambda a, b: a + b, scores)

print(total)
