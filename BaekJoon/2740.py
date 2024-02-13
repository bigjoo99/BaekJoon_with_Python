N, M = map(int, input().split())
matrix_A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
matrix_B = [list(map(int, input().split())) for _ in range(M)]

result = [[0]*K for _ in range(N)]

for i in range(N):
    for j in range(K):
        x = 0
        for k in range(M):
            x += matrix_A[i][k] * matrix_B[k][j]
        result[i][j] = x

for val in result:
    print(*val)
