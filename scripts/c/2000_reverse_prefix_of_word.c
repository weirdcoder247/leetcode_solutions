#include<stdio.h>

void moo(){
    /* do something and don't return a value */
    printf("Print Successful!!!");
    return;
};

unsigned int main(){
    moo();
    printf("\nPrint Success in Main as well!!!");
    return 0;
};
