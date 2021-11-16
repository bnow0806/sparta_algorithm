input = "abcabcabcabcdededededede"
# 2abcabc2dedede

def string_compression(string):
    n=len(string)
    compression_length_array=[]

    for split_size in range(1, n//2, 1):    #n 고정

        splited = [

            string[i:i+split_size] for i in range(0,n,split_size)
        ]
        print(splited)

        count =1
        compressed =""
        count_array=""  #압출률 디버깅
        for j in range(1, len(splited)):        #마지막 포함
            prev, cur = splited[j-1], splited[j]

            if prev == cur: #같다면
                count+=1
            else:   #같지 않다면 #이전까지 압축한 내용을 저장
                if count>1:
                    compressed+=(str(count)+prev)
                    #count_array += str(count)
                else:
                    compressed +=prev

                count_array += str(count)
                count=1 #초기화

        #마지막 문자 처리
        if count>1:
            compressed += (str(count) + splited[-1])
        else:
            compressed += splited[-1]

        count_array += str(count)

        print(compressed)
        print(count_array)

        compression_length_array.append(len(compressed))
    return min(compression_length_array)


#해설
# def string_compression_2(string):
#     n = len(string)
#     compression_length_array = []  # 1~len까지 압축했을때 길이 값
#
#     for split_size in range(1, n // 2 + 1):
#         compressed = ""
#         # string 갯수 단위로 쪼개기 *
#         splited = [
#             string[i:i + split_size] for i in range(0, n, split_size)
#         ]
#         count = 1
#
#         for j in range(1, len(splited)):
#             prev, cur = splited[j - 1], splited[j]
#             if prev == cur:
#                 count += 1
#             else:  # 이전 문자와 다르다면
#                 if count > 1:
#                     compressed += (str(count) + prev)
#                 else:  # 문자가 반복되지 않아 한번만 나타난 경우 1은 생략함
#                     compressed += prev
#                 count = 1  # 초기화
#         if count > 1:
#             compressed += (str(count) + splited[-1])
#         else:  # 문자가 반복되지 않아 한번만 나타난 경우 1은 생략함
#             compressed += splited[-1]
#
#         print(compressed)
#         compression_length_array.append(len(compressed))
#
#     return min(compression_length_array)  # 최솟값 리턴

print(string_compression(input))  # 14 가 출력되어야 합니다!