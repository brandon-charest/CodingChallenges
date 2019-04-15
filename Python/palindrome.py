
test_list = ["banana", "racecar", "Madam", "rotor", "boat", "cat"]

def palindrome(list):

    for word in list:
        if word.lower() == word.lower()[::-1]:
            print(f'{word} is a palindrome')
        else:
            print(f'{word} is not a palindrome')

palindrome(test_list)
