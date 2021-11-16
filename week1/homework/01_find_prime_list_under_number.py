input = 20


def find_prime_list_under_number(number):
    prime_array =[]
    # input 보다 작은 수의 모임 만들기
    for element in range(2, number+1):  #n<- 2~number
        prime_array.append(element)

    #print(prime_array)

    #print(prime_array)
    for prime_number in prime_array:
        #소수의 배수 없애기
        for n in range(round(input/prime_number)+1):
            #n이 2 이상일때 제거
            if n>=2:
                #print(prime_number," ",n)
                delete_number=prime_number * n
                if delete_number in prime_array:    #제거대상이 배열안에 있을때
                    prime_array.remove(delete_number)

    #print(prime_array)

    return prime_array


result = find_prime_list_under_number(input)
print(result)
