input = "011110"

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    last_element = None #dummy 값 할당
    string_array =[]
    for element in string:
        if element == last_element:
            continue
        else:
            string_array.append(element)
            last_element=element

    #print(string_array)
    number_reverse_zero = string_array.count("0")
    number_reverse_one = string_array.count("1")

    result=min(number_reverse_zero,number_reverse_one)

    return result


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)