''' Write a C Program to check if two numbers are equal without using the bitwise operator. '''

#include <stdio.h>

int main() {
    // Write C code here
    int a,b;
    scanf("%d %d",&a,&b);
    if((a^b)==0){
        printf("Same");
    }
    else{
        printf("Not Same");
    }


    return 0;
}
