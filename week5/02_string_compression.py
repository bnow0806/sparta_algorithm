from queue import Queue
#input = "abcabcabcabcdededededede"
         #2abcabc2dedede
input="aabbaccc"	# -> 7
#input="ababcdcdababcdcd"	# -> 9
#input="abcabcdede"	# -> 8
#input="abcabcabcabcdededededede"	# -> 14
#input="xababcdcdababcdcd"	# -> 17

#1. len(string)의 길이에서 /2 한 길이부터 자르기 시작 -> n
#2. queue 에서 n개의 문자열 꺼내기, 그다음 n개랑 같은지 비교
#3. 같으면 (value + 문자열) 형태로 저장
#4. + 남은 문자열의 개수 출력, 문자열이 끝날때 까지 반복 ->pop 하면 안됨...
#5. 문자열의 개수 출력

def string_compression(string):

    length = (len(string))
    half_length = int(length/2)
    answer=[[] for i in range(half_length+1)]   #딕셔너리형 배열

    queue = list(string)
    for i in range(half_length,0,-1):
        # print(i)   #12,11,...,2,1

        #1. n개 대로 문자열 쪼개기
        while len(queue) >= 2*i:
            first_queue = queue[:i]
            second_queue = queue[i:2*i]

            #print(i,first_queue,second_queue)

            if first_queue == second_queue:
                first_queue = [queue.pop(0) for idx in range(i)]
                second_queue = [queue.pop(0) for idx in range(i)]
                first_queue.insert(0,2)
                answer[i]+=first_queue

            elif len(string)!=len(queue):  #처음이 아니고, 문자열이 같지 않을때
                answer[i]+=queue.pop(0) #남은 문자열 하나씩 집어넣기

            else:
                break

        answer[i]+=queue    #나머지 부분 합치기
        # for문을 위한 초기화
        queue=list(string)
        count=0
        #answer[i].merge()

        print(i, answer[i])
        #print(len(answer[6]))

    #5.위에서 부터 검색 후 출력
    for i in range(half_length, 1, -1):
        if len(answer[i])!=0 and isinstance(answer[i][0],int):    #앞자리가 숫자이면
            return len(answer[i])


    return length


print(string_compression(input))  # 14 가 출력되어야 합니다!