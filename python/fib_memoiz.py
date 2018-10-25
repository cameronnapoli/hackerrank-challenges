import time


def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


memoiz = []
def fib_mem(n):
    global memoiz
    memoiz = [None]*n
    return fib_mem_helper(n)
def fib_mem_helper(n):
    global memoiz
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        if memoiz[n-1] != None:
            f1 = memoiz[n-1]
        else:
            f1 = fib_mem_helper(n-1)
            memoiz[n-1] = f1
        if memoiz[n-2] != None:
            f2 = memoiz[n-2]
        else:
            f2 = fib_mem_helper(n-2)
            memoiz[n-2] = f2
        return f1 + f2


def fn_call(fn, n):
    start_time = time.time()
    t = fn(n)
    print("Calling %s n: %s" % (fn, n))
    print("Result: %s" % t)
    print("--- %s seconds ---\n" % (time.time() - start_time))



fn_call(fib_mem, 300)
fn_call(fib, 55)
