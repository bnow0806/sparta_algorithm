seat_count = 9
vip_seat_array = [4, 7]
# 예전에 만들었던 fibo_dynamic_programming 에서 가져오면 됩니다!
memo = {
    1: 1,  # 이 문제에서는 Fibo(1) = 1, Fibo(2) = 2 로 시작합니다!
    2: 2
}

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):

    fibo_array=[]

    fixed_seat_array.append(total_count+1)
    #print(fixed_seat_array) #[4,7,10]

    fibo_array.append(fixed_seat_array[0]-1)
    for index in range(1,len(fixed_seat_array)):  #0,1,2

        vacant_count = fixed_seat_array[index]-fixed_seat_array[index-1]-1
        fibo_array.append(vacant_count)

    #print(fibo_array)

    sum=1
    for n in fibo_array:
        #print(n)
        sum*=fibo_dynamic_programming(n,memo)

    return  sum





def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))