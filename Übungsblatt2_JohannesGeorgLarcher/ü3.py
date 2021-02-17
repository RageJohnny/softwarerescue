import time


def it_fib(n):
        a, b = 0, 1
        for i in range(0, n):
            a, b = b, a + b
        return a




def rec_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)

start = time.time()
rec_fib(35)
end = time.time()
duration = end - start

start = time.time()
it_fib(35)
end = time.time()
duration = end - start

print(duration)



