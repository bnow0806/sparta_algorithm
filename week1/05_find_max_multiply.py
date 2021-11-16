input = [0, 3, 5, 6, 1, 2, 4]

#4+9=13
#4*9=36
#4+1=5
#4*1=4

def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    sum=0
    for element in array:
        if (sum<=1 or element <= 1):    #처음, sum<=1인 경우 고려
            sum=sum+element
        else:
            sum =sum*element

    return sum


result = find_max_plus_or_multiply(input)
print(result)