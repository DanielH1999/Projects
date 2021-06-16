#include<stdlib.h>
#include<stdio.h>

int noargs(int in)
{
    printf("dame un numero...\n");
    scanf("%d", &in);
    return in;
}

int esPrimo(int in)
{
    int i = 2;
    if(in < i)
    {
        return 0;
    }
    for(i = 2; i < in; i++)
    {
        if(in % i == 0)
        {
            return 0;
        }
    }
    if(in == i)
    {
        return 1;
    }
}

void main(int argc, char* argv[])
{
    int input;

    if(argc < 2)
    {
        input = noargs(input);
    }
    else
    {
        input = atoi(argv[argc - 1]);
    }

    if(esPrimo(input))
    {
        printf("%d es primo\n", input);
    }
    else
    {
        printf("%d no es primo\n", input);
    }
}
