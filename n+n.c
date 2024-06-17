#include<stdlib.h>
#include<stdio.h>

int input;

void noargs(void)
{
    printf("suma de componentes de...\n");
    scanf("%d", &input);
}

void main(int argc, char* argv[])
{
    int suma = 0;
    if(argc != 2)
    {
        noargs();
    }
    else
    {
        input = atoi(argv[argc - 1]);
    }
    for(int i = input; i > 0; i--)
    {
        suma += i;
    }
    printf("%d\n", suma);
}
