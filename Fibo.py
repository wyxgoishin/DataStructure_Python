def calFibo(n):
    if n < 1:
        return -1
    pre, cur = 0, 1
    for i in range(3, n+1):
        pre, cur = cur, pre + cur
    return cur

print(calFibo(7))