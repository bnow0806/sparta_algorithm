genres = ["classic", "pop", "classic", "classic", "pop"]
plays =  [500,        600,     150,       800,     2500]



def get_melon_best_album(genre_array, play_array):
    # 구현해보세요!
    answer=[]
    n= len(genre_array)
    #장르 선정
    array_index_classic = []
    array_index_pop = []
    for index in range(n):
        if genre_array[index] == "classic":
            array_index_classic.append(index)
        else:
            array_index_pop.append(index)

    print(array_index_classic, array_index_pop)

    sum_classic =0
    sum_pop =0
    for index in range(n):
        if index in array_index_classic:
            sum_classic += play_array[index]
        else:
            sum_pop +=play_array[index]

    #장르내 2곡 선정
    dict = {}
    for index in range(n):
        dict[index] = play_array[index]
    print(dict)

    dict_classic ={}
    dict_pop = {}

    for k,v in dict.items():
        if k  in array_index_classic:
            dict_classic[k] = v
        elif k  in array_index_pop:
            dict_pop[k] = v

    print(dict_classic,dict_pop)

    #정렬 by value
    sorted_keys_classic = sorted(dict_classic, key=dict_classic.get)
    sorted_keys_pop = sorted(dict_pop, key=dict_pop.get)
    print(sorted_keys_classic,sorted_keys_pop)

    #pop 먼저, classic 먼저 선택
    if sum_pop > sum_classic:
        answer.append(sorted_keys_pop[-1])
        answer.append(sorted_keys_pop[-2])
        answer.append(sorted_keys_classic[-1])
        answer.append(sorted_keys_classic[-2])
    else:
        answer.append(sorted_keys_classic[-1])
        answer.append(sorted_keys_classic[-2])
        answer.append(sorted_keys_pop[-1])
        answer.append(sorted_keys_pop[-2])


    return answer


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!