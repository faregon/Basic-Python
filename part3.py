from datetime import date


def add(x):
    return x+1

def sub(x):
    return x-1


# f = add(8)
# print(f)

list = [add,sub]
print(list[0](8))
print(list[1](9))

def applyAll(a, b):
    result = a
    for i in b:
        result = i(result)
    return result


print(applyAll(0, [add, add, add]))

def mymap(func, lst):
    result = []
    for e in lst:
        result.append(func(e))
    return result

a = mymap(add, [1,23])
for i in a:
    print(i)


def even(x):
    return x % 2 == 0


filter_a = filter(even, [1, 2, 3, 4, 5, 6])
for i in filter_a:
    print(i)

def myfilter(func, lst):
    result = []
    for e in lst:
        result.append(func(e))
    return result

filter_b = myfilter(even, [1, 2, 8, 3, 4, 5, 6])
for i in filter_b:
    print(i)


def funny(p):
    return p(5)

map_c = map(funny, [add, sub, even])

for i in map_c:
    print(i)


datetime = date.today().isocalendar()[1]

print(datetime)