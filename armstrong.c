#include<stdio.h>
#include<stdlib.h>

int pot(int a, int b)
{
    int og = a;
    for(int i = 1; i < b; i++)
    {
        a = a * og;
    }
    return a;
}

int main(int argc, char* argv[])
{
    int in, cp, res, resultado = 0;
    if(argc > 1)
    {
        in = atoi(argv[argc - 1]);
    }
    else
    {
        printf("numero: ");
        scanf("%d", &in);
    }

    cp = in;

    while(cp > 0)
    {
        int temp;
        res = cp % 10;
        cp /= 10;
        temp = pot(res, 3);
        resultado += temp;
    }
    if(resultado == in)
    {
        printf("%d es un \"numero armstrong\"\n", in);
    }
    else
    {
        printf("%d no es un \"numero armstrong\"\n", in);
    }
}
