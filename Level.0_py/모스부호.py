def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
    letter = letter.split(' ')
    answer = []
    for i in letter:
        answer.append(morse[i])
    return ''.join(answer)

#letter =".... . .-.. .-.. ---"	, result="hello"
#letter에 적혀있는 모스부호를 보고 영어 소문자로 바꾼 문자열을 return