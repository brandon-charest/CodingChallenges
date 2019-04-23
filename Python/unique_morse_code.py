"""
804. Unique Morse Code Words

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation:
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--."
"""
import string

def unique_morse_code(word_list):
    morse_letters = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
                     "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
                     "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
                     "-.--", "--.."]
    alphabet = list(string.ascii_lowercase)

    morse_code = dict(zip(alphabet, morse_letters))

    unique_words_set = set()
    unique_words_count = 0

    for word in word_list:
        result = ""
        for c in word:
            if c in morse_code.keys():
                result +=morse_code[c]
        if result not in unique_words_set:
            unique_words_count += 1
            unique_words_set.add(result)

    return unique_words_count



words = ["gin", "zen", "gig", "msg"]
print(unique_morse_code(words))