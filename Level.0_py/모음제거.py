def solution(my_string):
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        my_string = my_string.replace(vowel, '')
    return my_string
#모음을 제거하여 다시 나열
# my_string="hi my name is kelly" result="h my nm s klly"