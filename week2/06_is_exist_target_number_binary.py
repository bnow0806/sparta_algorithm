finding_target = 39
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    # 구현해보세요!   #값으로 접근하니 어려워짐 -> index로 비교하기
    try:                            #array index error 대비
        first_number = array[0]
        last_number = array[len(array) - 1]
        print("fir,last :", first_number, ",", last_number)
    except:
        return False

    # 16 -> 8 -> 4 -> 2
    mid_number = (first_number + last_number) // 2
    mid_index = mid_number - first_number + 1
    print("mid_number", mid_number)
    print("mid_index", mid_index)

    # 절반으로나누기
    print("array[:mid_number]", array[:mid_index-1])  # 처음 ~ mid_index 이전
    print("array[mid_number:]", array[mid_index:])  # mid_index ~ 끝

    ret_value = None

    if target != mid_number and len(array) == 1:
        print("len=1")
        return False

    if target == mid_number:
        print("target == mid_number")
        return True

    elif target < mid_number:
        print("target < mid_number")
        ret_value = is_existing_target_number_binary(target, array[:mid_index-1])

    else:
        print("target > mid_number")
        ret_value = is_existing_target_number_binary(target, array[mid_index:])

    return ret_value


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)

# print("Test ",None==False)