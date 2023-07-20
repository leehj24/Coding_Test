class sil:
    def solution(my_string, overwrite_string, s):
       return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]
if __name__ == '__main__':
   sil().solution()