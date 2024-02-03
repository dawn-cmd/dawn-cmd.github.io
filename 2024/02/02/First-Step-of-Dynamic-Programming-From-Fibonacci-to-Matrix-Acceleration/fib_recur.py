import time
called_count = 0
def fib(i):
    global called_count
    called_count += 1
    return i if i < 2 else fib(i - 1) + fib(i - 2)

def main():
    n = int(input())
    start_time = time.time()
    result = fib(n)
    end_time = time.time()
    print(f"The fib function took {end_time - start_time} seconds to execute.")
    print(result)
    print(f"The fib function was called {called_count} times.")

if __name__ == '__main__':
    main()
