# %%
import time

# %%
def grid(m, n):
    if m<=0 or n<=0:
        return 0
    if m==1 and n==1:
        return 1
    else:
        return grid(m-1, n) + grid(m, n-1)

# %%
def memoized_grid(m, n, data=None):
    if data is None:
        data = {}
    if (m,n) in data:
        return data[(m,n)]
    if (n,m) in data:
        return data[(n,m)]
    # if (n,m) in data:
    #     return data[(n,m)]
    if m<=0 or n<=0:
        return 0
    if m==1 or n==1:
        return 1
    else:
        data[(n,m)] = data[(m,n)] = memoized_grid(m-1, n, data) + memoized_grid(m, n-1, data)
        return data[(m,n)]
# %%
a,b = 1000, 1000

t1 = time.time()
memoized_grid(a, b)
print("Execution Time: {tm:.2f}, seconds".format(tm=time.time()-t1))

# t1 = time.time()
# grid(a, b)
# print("Execution Time: {tm:.2f}, seconds".format(tm=time.time()-t1))

# %%
