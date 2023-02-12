import itertools
import functools


def Subset(list1):
    if len(list1) <= 1:
        yield list1
        yield []
    else:
        for item in Subset(list1[1:]):
            yield [list1[0]]+item
            yield item

def xor(list2):
    res = 0
    for i in range(1, len(list2) + 1):
        for arr in itertools.combinations(list2, i):
            temp = functools.reduce(lambda x, y: x ^ y, list(arr))
            res += temp
    return res

l1 = [1,3]

r = [x for x in Subset(l1)]

r.sort()
print(r)
print(xor(l1))
