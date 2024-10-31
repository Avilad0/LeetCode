# def simpleGeneratorFun():
#     yield 1            
#     yield 2            
#     yield 3            

# t = simpleGeneratorFun()

# print(next(t))
# print(next(t))

# for i in t:
#     print(i)


def fib(limit):
    a, b = 0, 1
    while b < limit:
        yield b
        a, b = b, a + b

x = fib(50)
for i in x:
    print(i)