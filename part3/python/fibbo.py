from functools import lru_cache

def memo(f):
    cache = {}
    def inner(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return inner

@memo
def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n-1) + fib1(n - 2)

# fib = lru_cache(maxsize=None)(fib1)

def fib3(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f1 + f0
    return f1

import time

def timed(f, *args, n_iter=100):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc

print(timed(fib3, 80000))
# print(fib3(8000))