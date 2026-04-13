#include <stdio.h>

int add(int a, int b) {
    // printf("Hello, World\n");
    // return 0;
    // int score = 60;
    // if (score >= 50) {
    //     printf("Pass\n");
    // }else {
    //     printf("Fail\n");
    // }
    int sum = a + b;

    // printf("%d\n", sum);
    return a + b;
}

int main() {
    printf("%d\n", add(3, 4));
}