cnt = 0

def hanoi_cnt(n,start,ending,sub):
    global  cnt
    if n == 1:
        cnt+=1
    else:
        hanoi_cnt(n-1, start,sub, ending)
        cnt +=1
        hanoi_cnt(n-1, sub, ending, start)
            
def hanoi(n,start,ending,sub):
    if n == 1:
        print(start, ending)
    else:
        hanoi(n-1, start,sub, ending)
        print(start, ending)
        hanoi(n-1, sub, ending, start)

n = int(input())

hanoi_cnt(n, '1','3','2')
print(cnt)
hanoi(n, '1','3','2')