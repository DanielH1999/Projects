#include<stdlib.h>
#include<stdio.h>

int input;

void noargs(void)
{
    printf("averiguar factores de...\n");
    scanf("%d", &input);
}

void main(int argc, char* argv[])
{
    if(argc != 2)
    {
        noargs();
    }
    else
    {
        input = atoi(argv[argc - 1]);
    }

    printf("Es divisible por:\n");

    for(int i = 1; i <= input; i++)
    {
        if(input % i == 0)
        {
            printf("%d\n", i);
        }
    }
}
