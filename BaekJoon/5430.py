T = int(input())

result_array = []

for _ in range(T):
    func = input()          # 함수 사용
    N = int(input())        # 배열 길이
    array = input()         # 배열 값
    
    arr = []
    
    for i in range(1,N-1):
        x = array[i].split('[')
        x = array[i].split(',')
        arr.append(x)  
        
    
    for fun in func:
        if fun == 'R':
            arr.sort(reverse =True)
        
        elif fun == 'D':
            if len(arr) == 0:
                print('error')
                break
            else:
                arr.pop(0)