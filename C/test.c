#include <stdio.h>

int main() {
    int myNum1;
    int myNum2;
    printf("Enter two numbers: \n");
    scanf("%d %d", &myNum1, &myNum2);
    int myNumResult = myNum1 + myNum2;
    if (myNumResult > 0) {
        printf("This number is positive\n");
    } else if (myNumResult < 0) {
        printf("This number is negative\n");
    }
    printf("%d + %d = %d ", myNum1, myNum2, myNumResult);
    printf("\nThe memory address is:\n");
    printf ("%p", &myNumResult);
    return 0;
}