
def reverse_words(s: str) -> str:
    result = ''
    temp = ''
    for i in range(len(s)):
        if s[i] is not ' ':
            temp += s[i]
        else:
            result += temp[::-1] + ' '
            temp =''
    result += temp[::-1]
    return result




x = "Let's take LeetCode contest"
print(reverse_words(x))