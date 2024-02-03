import time

def main():
    n = int(input())
    fib = [0] * (n + 2)
    fib[1] = 1
    start_time = time.perf_counter()
    for i in range(2, n + 2):
        fib[i] = fib[i - 1] + fib[i - 2]
    end_time = time.perf_counter()
    print(fib[n])
    print("Execution time:", end_time - start_time, "seconds")

if __name__ == '__main__':
    main()
