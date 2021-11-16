#numbers = [2,3,4,5]
numbers = [2,3,1]
target_number = 0
count =0

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    # 구현해보세요!
    #                                                 target : 3
    # -1/ 1, 1, 1, 1 -> function(array[1:n],target+1)   4
    # -1, 1/ 1, 1, 1 -> function(array[1:n],target-1)   3
    # -1, 1, 1/ 1, 1 -> function(array[1:n],target-1)   2
    # -1, 1, 1, 1/ 1 -> True or False                   1

    global count

    n = len(array)
    #print("n", n)

    if n<=1:
        if abs(array[0]) == abs(target):    #최종 target이 -1인 경우
            print("target matched", array)
            count+=1
            return

        else:
            return

    #minus
    print("n=",n,"array[1:n]",array[1:n],"target",target)
    ret_minus = get_count_of_ways_to_target_by_doing_plus_or_minus(array[1:n], target + array[0])

    #plus
    ret_plus = get_count_of_ways_to_target_by_doing_plus_or_minus(array[1:n], target - array[0])

    return count


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!