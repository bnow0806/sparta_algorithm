s = "(())()"

# (())()
# 2 -2 +1 -1 =0 O
# )()(
# -1+1-1+1 =0 X
# ())(
# 1-1-1+1 = 0 X
# ((()())(
# 처음 시작 (, 마지막 ), ()합이 0

# 바로직전 열린 괄호 저장, 닫힌 괄호 - stack
#((()
#1. ["("]
#2. ["(","("]
#3. ["(","(","("]
#4. ["(","("] ->X

def is_correct_parenthesis(string):
    # 구현해보세요!
    array=list(string)  #string[i]로 해도됨
    print(array)

    #처음 시작 검사
    if array[0] != "(":
        return False

    #마지막 검사
    if array[-1] != ")":
        return False

    sum = 0
    for i in range(len(array)):
        data = array.pop(0)

        if data == "(":
            sum +=1
        elif data == ")":
            sum -=1

    if sum != 0:
        return False

    return True


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!