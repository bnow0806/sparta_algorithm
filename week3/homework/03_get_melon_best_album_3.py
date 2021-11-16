genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# 1. 장르 별로(key) 재생된 횟수(value)를 저장
# - classic 몇 회, pop 몇 회
# - [classic:몇 회, pop : 몇회], 정렬
# 2. 장르 별로 곡의 정보(인덱스, 재생횟수) 배열로 저장
# - {classic : [[0,500],[2,150],[3,800]], pop : [[1,600], [4,2500]]}
# 3. 장르 별 곡의 재생횟수를 기준으로 정렬, 상위 2가지 저장
# - [[3,800],[0,500],[2,150]] -> [3,0]
# - [[4,2500], [1,600]] -> [4,1]

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    total_genre_play ={}
    index_play_array=0
    genre_play_list_info ={}
    answer =[]

    for genre in genre_array:
        #print(genre)
        if genre not in total_genre_play:   #key 가 없을 경우(최초 등록)
            total_genre_play[genre] = play_array[index_play_array]
            genre_play_list_info[genre] = []
            genre_play_list_info[genre].append([index_play_array, play_array[index_play_array]])
            index_play_array +=1
        else:
            total_genre_play[genre] += play_array[index_play_array]
            genre_play_list_info[genre].append([index_play_array, play_array[index_play_array]])
            index_play_array +=1

    print("total_genre_play",total_genre_play)
    sorted_total_genre_play = sorted(total_genre_play.items(), key=lambda item:item[1], reverse=True)
    print("total_genre_play.items()",total_genre_play.items())
    print("sorted_total_genre_play",sorted_total_genre_play)    #list 접근 & tuple접근
    print(genre_play_list_info)

    for key,value in sorted_total_genre_play:   #tuple에서 값을 꺼내는 법
        final_list_info=genre_play_list_info[key]
        #print(final_genre_play_list_info)  #[[1, 600], [4, 2500]]
        #이중 배열을 정렬할 때는 items를 안 붙이고, 바로 넣는다.
        sorted_final_list_info = sorted(final_list_info, key=lambda item:item[1], reverse=True)

        for i in range(2):
            value = sorted_final_list_info[i][0]
            answer.append(value)

    return answer


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!

# a=[[1,2],[3,4]]
# print("a",sorted(a, key=lambda item:item[0], reverse=True))