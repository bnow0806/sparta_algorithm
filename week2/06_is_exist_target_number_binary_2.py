finding_target = 16
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

#index로 이동, 값비교시에만 array접근
def is_existing_target_number_binary(target, array):
    current_min = 0                 #0
    current_max = len(array) - 1    #15
    current_guess = (current_min + current_max) // 2    #7

    #       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    #1단계 최솟값                시돗값                         최댓값
    #2단계                          최솟값      시돗값          최댓값
    #3단계                                        최솟값        최댓값
    #4단계                                                최솟값 최댓값
    #                                                    (시돗값)
    #5단계                                                       최솟값(최댓값,시도값)

    count =0
    while current_min <= current_max:           #0<=15
        count+=1
        if array[current_guess] == target:
            print(count)
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1

        #중간값을 인덱스로 동기화
        current_guess = (current_min + current_max) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)