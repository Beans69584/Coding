#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <windows.h>
int main(int argc, char *argv[])
{
    int a, b, c;
    printf("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n");
    printf("Enter your choice: ");
    scanf("%d", &c);
    printf("Enter first number: ");
    scanf("%d", &a);
    printf("Enter second number: ");
    scanf("%d", &b);
    switch (c)
    {
    case 1:
        printf("Sum = %d", a + b);
        break;
    case 2:
        printf("Difference = %d", a - b);
        break;
    case 3:
        printf("Product = %d", a * b);
        break;
    case 4:
        printf("Quotient = %d", a / b);
        break;
    default:
        printf("Invalid choice");
    }
    printf("\n");
    Sleep(2000);
    system("cls");
    return 0;
}