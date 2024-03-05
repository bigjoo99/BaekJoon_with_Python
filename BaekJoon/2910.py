from collections import Counter

n, c = map(int, input().split())
arr = list(map(int, input().split()))

arr_cnt = Counter(arr).most_common()

for x,y in arr_cnt:
    for _ in range(y):
        print(x, end=' ')