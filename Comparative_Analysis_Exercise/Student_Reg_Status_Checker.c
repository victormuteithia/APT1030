// Student Registration Status Checker in C
#include <stdio.h>


int main() {
    char stu_name[30];
    int units;

    printf("Enter your name: ");
    scanf("%s", stu_name);
    printf("Enter no. of units registered: ");
    scanf("%d", &units);

    if (units > 7) {
        printf("---------------------------------------\n");
        printf("Student Name: %s\n", stu_name);
        printf("Registered Units: %d\n", units);
        printf("Status: Overload - Approval Required.\n");
        printf("---------------------------------------\n");
    } else {
        printf("---------------------------------------\n");
        printf("Student Name: %s\n", stu_name);
        printf("Registered Units: %d\n", units);
        printf("Status: Registration Accepted.\n");
        printf("---------------------------------------\n");
    }

    return 0;

}