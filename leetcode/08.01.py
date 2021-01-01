def waysToStep(n):
    if n < 3:
        return n
    elif n == 3:
        return 4
    ppre, pre, cur, nxt = 0, 1, 2, 4
    for i in range(4, n+1):
        ppre, pre, cur, nxt = pre, cur, nxt, pre + cur + nxt
    return nxt


print(waysToStep(900750))