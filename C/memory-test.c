#include <stdio.h>
#include <string.h>
#include <windows.h>

int main()
{
    memory_test();
    return 0;
}

void memory_test()
{
    int *ptr = (int *)malloc(5 * sizeof(int));
    for (int i = 0; i < 5; i++)
    {
        ptr[i] = i + 1;
    }
    for (int i = 0; i < 5; i++)
    {
        printf("%d ", ptr[i]);
    }
    printf("\n");
    ptr = (int *)realloc(ptr, 10 * sizeof(int));
    for (int i = 5; i < 10; i++)
    {
        ptr[i] = i + 1;
    }
    for (int i = 0; i < 10; i++)
    {
        printf("%d ", ptr[i]);
    }
    printf("\n");
    free(ptr);
    ptr = NULL;
    printf("%d", ptr);
}