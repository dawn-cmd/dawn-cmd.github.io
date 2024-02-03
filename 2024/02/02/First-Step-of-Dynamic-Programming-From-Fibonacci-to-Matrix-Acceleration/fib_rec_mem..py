import time

cache = []

def fib(i):
    global cache
    if cache[i] != 0:
        return cache[i]
    cache[i] = i if i < 2 else fib(i - 1) + fib(i - 2)
    return cache[i]

def main():
    global cache
    n = int(input())
    cache = [0] * (n + 1)
    start_time = time.perf_counter()
    result = fib(n)
    end_time = time.perf_counter()
    print(result)
    print(f"The fib function took {end_time - start_time} seconds to execute.")

if __name__ == '__main__':
    main()
