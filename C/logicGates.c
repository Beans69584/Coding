#include <stdio.h>
#include <string.h>
#include <windows.h>

int main()
{
    int a, b, c;
    printf("1.AND\n2.OR\n3.NOT\n4.XOR\n5.XNOR\n6.NAND\n7.NOR\n");
    printf("Enter your choice: ");
    scanf("%d", &c);
    printf("Enter (0/1): ");
    scanf("%d", &a);
    printf("Enter (0/1): ");
    scanf("%d", &b);
    system("cls");
    switch (c)
    {
    case 1:
        printf("AND = %d", a & b);
        break;
    case 2:
        printf("OR = %d", a | b);
        break;
    case 3:
        printf("NOT = %d", !a);
        break;
    case 4:
        printf("XOR = %d", a ^ b);
        break;
    case 5:
        printf("XNOR = %d", !(a ^ b));
        break;
    case 6:
        printf("NAND = %d", !(a & b));
        break;
    case 7:
        printf("NOR = %d", !(a | b));
        break;
    default:
        printf("Invalid choice");
    }
}