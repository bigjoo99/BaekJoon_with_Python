import sys

input = sys.stdin.readline

T = int(input())

result = []

for _ in range(T):
    N = int(input())
    race = list(map(int, input().split()))
    
    arr = [0]*201       # 6명 참가 했는지 확인용 list
    Team_list = []      # 6명 참가한 Team list
    Team = [[0] for _ in range(201)]    # 6명 있는 Team 개인 점수   
    Team_score = []     # Team의 최종 점수
    
    for i in range(N):  # race안에서 참가한 팀원 수 확인
        arr[race[i]] += 1
    
    for i in range(len(arr)):       # 만약 6명 참가한 팀이 있다면 Team_list에 추가
        if arr[i] == 6:
            Team_list.append(i)

    score = 1
    
    for i in range(N):
        x = race[i]
        if race[i] in Team_list:
            Team[x].append(score)
            score += 1
        
    Team_sort = [sorted(row) for row in Team]
    
    for i in range(201):
        if i not in Team_list:
            for j in range(6):
                Team_sort[i].append(0)
                Team[i].append(0)
                
    for i in Team_list:
        Team_sort[i][0] = Team_sort[i][1] + Team_sort[i][2] + Team_sort[i][3] + Team_sort[i][4]
    
    Team_sort.sort(key=lambda x :(-x[0], x[5]))
    
    for i in range(201):
        if Team[i][5] == Team_sort[0][5]: 
            result.append(i)

for i in result:
    print(i)