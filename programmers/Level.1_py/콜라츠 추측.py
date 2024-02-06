def solution(n):
    Count=0
    while n!=1:
        if n%2==0:
            n=n//2
            
        else:
            n= n*3+1
        Count+=1
    if Count >=500:
        Count =-1
    return Count    

def collatz(num):
    for i in range(500):
    	if num == 1:
            return i
        num = num / 2 if num % 2 == 0 else num*3 + 1   
    return -1
    
#입력된 수가 짝수라면 2로 나눕니다. 
#입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
#결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
#단, 작업을 500번을 반복해도 1이 되지 않는다면 –1을 반환해 주세요.
#예를 들어, 입력된 수가 6이라면 6→3→10→5→16→8→4→2→1 이 되어 총 8번 만에 1이 됩니다.