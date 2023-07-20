#include <stdio.h>
#define LEN_INPUT 10

int main(void) {
    char s1[LEN_INPUT];
    scanf("%s", s1);
    int i = 0;
    while (s1[i]){
        if (isupper(s1[i])){ //소문자 판별
            s1[i]= tolower(s1[i]); //대문자로 변경
        }
        else if (islower(s1[i])){ //대문자 판별
            s1[i]= toupper (s1[i]); //소문자로 변경
        }
        i++;
    }
    printf(s1);
    return 0;
}
