def solution(arr, delete_list):
    answer = []
    for i in arr:
        if i not in delete_list:
            answer.append(i)
    return answer
# arr배열에 delete_list배열의 원소를 제외한 원소들을 나열
# arr=[293,1000,395,678, 4] result =[94,777,104,1000,1,12]