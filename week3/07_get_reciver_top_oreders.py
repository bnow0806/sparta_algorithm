top_heights = [6, 9, 5, 7, 4]

# [0, 0, 2, 2, 4]
# [0, 0, 0, 0, 0]

# <- <- <- <- <- 레이저의 방향
# 6  9  5  7  4
#[0, 0, 0, 0, 4]

# 6  9  5  7
#[0, 0, 0, 2, 4]

def get_receiver_top_orders(heights):
    answer = [0] * len(heights)

    while heights:
        #전체 비교 대상이 줄어드므로 stack, pop을 사용함
        height = heights.pop()  #4

        # 복사 후 pop을 한번 더 써서 값을 보는것보다, idx를 사용하는 것이 편리함
        for idx in range(len(heights)-1,-1,-1):  #3,2,1,0
            print(idx)
            if heights[idx] > height:
                answer[len(heights)]=idx+1  #4
                break

    return answer

# def get_receiver_top_orders(heights):
#
#     ret_array = []
#
#     for i in range(len(heights)):   #5번
#         pop_value=heights.pop()  #4  #stack_height:[6, 9, 5, 7]
#         print("stack_height", heights)
#         #print(stack_height[-1]) #peek 대신
#
#         #stack에 copy하기
#         stack_copy = []
#         for element in heights:
#             stack_copy.append(element)
#
#         #[6.9.5.3.4]
#         while len(stack_copy) >=1 and stack_copy[-1] < pop_value:  #7>4
#             stack_copy.pop()
#
#             if len(stack_copy) ==0:
#                 print("len =0")
#                 break
#
#         print(len(stack_copy))
#         ret_array.append(len(stack_copy))
#
#     ret_array.reverse()
#
#     return  ret_array



print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!