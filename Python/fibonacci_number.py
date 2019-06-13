
def fib(num):
    if num == 0:
        return 0
    elif num < 2:
        return 1

    return fib(num - 1) + fib(num - 2)


fib_num = 2
print(fib(fib_num))
