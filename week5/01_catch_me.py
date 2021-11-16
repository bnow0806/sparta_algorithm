from collections import deque

c = 11
b = 2

# C = C+time
# B = B-1, B+1, 2*B
# B의 위치 추정  #모두 확인 이므로 BFS
# time = 1
#1. 1
#2. 3
#3. 4
# time = 2
#1-1. 1-1 = 0    2-1. 3-1 =2    ->위치, 시간 queue
#1-2. 1+1 = 2    2-2. 3+1 =4
#1-3. 1*2 = 2    2-3. 3*2 =6

#visited[위치] = {시간}
#visited[1] = {1:True,3:True,4:True}
#visited[2] = {0:True,2:True,4:True,6:True}

def catch_me(cony_loc, brown_loc):

    time =0
    visited = [{} for i in range(200001)]
    queue = deque()
    queue.append((brown_loc,0))   #위치, 시간 - tuple 형태

    #print(queue.popleft())

    while cony_loc < 200001:    #cony_loc 고정, queue 탐색
        #C 위치 추정
        cony_loc+=time          #time : 0,1,2,3,4...
        print("test_time",time)
        print("cony_loc",cony_loc)
        # 탈출조건
        if time in visited[cony_loc]:
            print("correct_cony_loc", cony_loc)
            return time

        for i in range(len(queue)): #앞에 time의 queue들은 모두 검색
            brown_loc, time = queue.popleft()  # queue에서 꺼냄

            #B 위치 추정    #방문 기록이 없다면 추가하여 검색 대상화
            new_time = time + 1

            new_brown_loc = brown_loc-1
            if new_brown_loc>=0 and new_time not in visited[new_brown_loc]:
                queue.append((new_brown_loc,new_time))
                visited[new_brown_loc][new_time] = True

            new_brown_loc = brown_loc+1
            if new_brown_loc<200001 and new_time not in visited[new_brown_loc]:
                queue.append((new_brown_loc,new_time))
                visited[new_brown_loc][new_time] = True

            new_brown_loc = brown_loc*2
            if new_brown_loc<200001 and new_time not in visited[new_brown_loc]:
                queue.append((new_brown_loc,new_time))
                visited[new_brown_loc][new_time] = True

            time+=1

        print("time",time)
        print("queue",queue)

    return None


print(catch_me(c, b))  # 5가 나와야 합니다!
#print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
#print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
#print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))