def fib(n: int) -> int:
    if n <= 1:
        return n
    grandparent = 0
    parent = 1
    current = 1
    for i in range(n - 1):
        current = parent + grandparent
        grandparent = parent
        parent = current
    return current

