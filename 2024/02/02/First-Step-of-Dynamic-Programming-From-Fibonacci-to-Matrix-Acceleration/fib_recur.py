import time
def fib(i):
    return i if i < 2 else fib(i - 1) + fib(i - 2)

def main():
    n = int(input())
    start_time = time.time()
    result = fib(n)
    end_time = time.time()
    print(f"The fib function took {end_time - start_time} seconds to execute.")
    print(result)

if __name__ == '__main__':
    main()
