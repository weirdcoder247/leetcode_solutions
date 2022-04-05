#include<stdio.h>

void moo(){
    /* do something and don't return a value */
    printf("Print Successful!!!");
    return;
}

int main(__attribute__((unused)) int argc, const char *argv[]){
    moo();
    printf("\nPrint Success in Main as well!!!");
    return 0;
}
