input = "abccba"


def is_palindrome(string):

    # n= len(string)
    # for i in range(n):
    #     if string[i] != string[n-1-i]:
    #         return False

    #abcba      abccba
    #bcb        bccb
    #c          cc
    #ok         []
    #           ok

    n=len(string)

    if n <= 1:
        print("string",string)
        print("n", n)
        return True

    if string[0] == string[-1]:

        print(string[1:-1])

        return is_palindrome(string[1:-1])

    else:
        return False







print(is_palindrome(input))