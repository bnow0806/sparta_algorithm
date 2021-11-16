current_r, current_c, current_d = 6, 3, 1
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #0
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  #10
]
current_room_map2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
#1. 현재 위치 청소
#2. 2-a 왼쪽,
#3. 2-b 왼쪽에 없다면 회전하고 2번으로 이동
#4. 2-c 네 방향 모두 청소 시, 후진 뒤 2번이동
#5. 4번이 안될때 멈춤

def get_d_index_when_rotate_to_left(d):
    return (d+3)%4

def get_d_index_when_go_back(d):
    return (d+2)%4

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):

    visited = []
    reverse_count =0
    #1. 현재 위치 청소
    cur_node = [r, c]
    visited.append(cur_node)
    temp_d=d

    while 1:
        #2. 2-a
        #d=0 ->3, 3->2, 2->1, 1->0
        #post_d = d
        #d = (d + 3) % 4
        temp_d = get_d_index_when_rotate_to_left(temp_d)
        back_d = get_d_index_when_go_back(temp_d)
        #print(temp_d,back_d)

        #d 에 따른 r,c의 변화 #북, 동, 남, 서
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        next_node = [cur_node[0]+dr[temp_d], cur_node[1]+dc[temp_d]]
        post_node =[cur_node[0]+dr[back_d], cur_node[1]+dc[back_d]]

        #2-a.
        if room_map[next_node[0]][next_node[1]] ==0 and (next_node not in visited):
            cur_node = next_node
            visited.append(cur_node)
            reverse_count =0

        # 2-b
        elif room_map[next_node[0]][next_node[1]]==1 or (next_node in visited):
            reverse_count +=1

        # 2-c.
        if reverse_count == 4:
            if room_map[post_node[0]][post_node[1]] == 0:
                cur_node = post_node
                reverse_count = 0
            # 2-d.
            else:
                break
        #print(visited)


    return len(visited)



# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map2))

# cur_node = [1,2]
# visted = [[1,3],[3,4]]
# if cur_node in visted:
#     print("True")
#