import  pytest


words = ['cat', 'window', 'defenestrate']
for w in words:
     print(w, len(w))

print ('###########################')
for i in range(10):
    print (i)


print ('###########################')

##这是函数
def hanshu(woshipython):
    print ('110')

hanshu(
 woshipython=1111
)

hanshu(
    woshipython='nihao'
)

a=[1,2,3]
print(*a)

def hanshu1(a=3,b=7):
    print(a*b)

hanshu1(a=10,b=15)



def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop(kind='nihao',arguments=10,keywords='guanjianci')

class A:
    def m_a(self):
        a=1
        print("A.m_a")
        print(a)


def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

fib(100)

print('**************************************')

fib2(120)