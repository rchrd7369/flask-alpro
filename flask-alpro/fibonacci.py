def generate_fibonacci(n):
    fib_series = [1, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series
