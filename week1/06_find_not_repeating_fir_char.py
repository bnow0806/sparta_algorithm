#input = "abacabade"
input = "abadabac"

def find_not_repeating_character(string):
    # 이 부분을 채워보세요!
    not_repeating_character_array =[]

    for element in string:
        if string.count(element) ==1:   #03_02로도 풀기 가능
            #return element
            not_repeating_character_array.append(element)

    for element in string:  #먼저 나온 element
        if element in not_repeating_character_array:    #그 안에 값이 있다면 반환
            return element

result = find_not_repeating_character(input)
print(result)