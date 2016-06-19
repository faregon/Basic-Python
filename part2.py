# def myfunc(a):
#     print("This is the parameter: " + a)
#
# myfunc(str([1,2,3]))
# myfunc("Hello world")
# def more(a,b):
#     print("a is " + a)
#     print("b is " +b)
#
# more("aa", "bb")
# def addone(a) :
#     a = a +1
#     return a
# b = addone(8)
# print(b)
# def upto (n):
#     return n *(n+1)//2
#
# b = upto(10)
# print(b)
#
#
# def addall(list):
#        print(sum(list))
# addall([1,2,3])
#
# def reverse(list):
#     print(list[::-1])
#
#
# reverse([1,3,4,5])

def minmax(list):
    print(min(list), max(list))


t = minmax([1,2,3,4,99,12,33])
print(t)

def evennumbers(list):
    for i in list:
        if i%2 == 0:
            print(i)

vev = evennumbers([2,7,8,9,13,99])
print(vev)

# def fib(n):
#      a,b = 0,1
#      while a<n:
#          print(a, end=' ')
#          a,b = b, a+b
#      print()
# fib(1000)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

t = fib(8)
print(t)

def inc_list(list):
     list += 1;
     return list

list2 = [1,2,3]
inc_list(list2)
print(list2)