def fib(n):
    print("call: ",n)
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)

def fib2(n):
    if n < 2:
        return 1
    a = [1 for _ in range(n)]
    a[0] = 1
    a[1] = 1
    for i in range(2,n):
        a[i] = a[i-1] + a[i-2]
    return a[n-1]
# recursive case
def hier(n):
    if n == 0:
        return 1
    return n*hier(n-1)

print(fib2(5))
print(hier(5))