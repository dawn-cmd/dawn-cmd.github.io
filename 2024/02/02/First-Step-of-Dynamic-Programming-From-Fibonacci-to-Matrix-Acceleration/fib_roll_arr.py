import time

def main():
    n = int(input())
    fib_i = 1
    fib_i_prev = 0
    start_time = time.perf_counter()
    for i in range(2, n + 1):
        fib_i, fib_i_prev = fib_i + fib_i_prev, fib_i
    end_time = time.perf_counter()
    print(fib_i)
    print("Execution time:", end_time - start_time, "seconds")

if __name__ == '__main__':
    main()
