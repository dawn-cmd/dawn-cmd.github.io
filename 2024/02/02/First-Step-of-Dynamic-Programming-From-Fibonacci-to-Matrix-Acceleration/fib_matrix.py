MOD = 1000000007

def main():
    n = int(input())
    print(fib(n))

def fib(n):
    if n < 2:
        return n
    st = [[1, 0, 0]]
    update_matrix = qpow([[1, 1, 0], [1, 0, 1], [0, 0, 0]], n - 1)
    return matrix_multiply(st, update_matrix)[0][0] % MOD 

def qpow(a, n):
    if n == 1:
        return a
    if n % 2 == 0:
        return qpow(matrix_multiply(a, a), n // 2)
    return matrix_multiply(a, qpow(matrix_multiply(a, a), n // 2))

def matrix_multiply(a, b):
    ans = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)): 
                ans[i][j] += a[i][k] * b[k][j] % MOD
    return ans

if __name__ == "__main__":
    main()
