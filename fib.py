# %%
import time
# %%

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

# %%
data = {}

def memoized_fib(n):
    if n in data:
        return data[n]
    else:
        if n <= 2:
            data[n] = 1
        else:
            data[n] = memoized_fib(n-1) + memoized_fib(n-2)
        return data[n]

# %%
tst = [1,5,30]
for t in tst:
    t1 = time.time()
    res = fib(t)
    print("Result: ", res)
    print("Execution Time: {tm:.2f} secs".format(tm = time.time()-t1))

# %%
tst = [1,2, 50]
for t in tst:
    t1 = time.time()
    res = memoized_fib(t)
    print("Result: ", res)
    print("Execution Time: {tm:.5f} secs".format(tm = time.time()-t1))
