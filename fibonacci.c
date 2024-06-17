#include<stdlib.h>
#include<stdio.h>

int main(int argc, char* argv[])
{
    int rango, limit = 2, a = 0, b = 1, c;

    if(argc > 1 && atoi(argv[argc - 1]) >= limit)
    {
        rango = atoi(argv[argc - 1]);
    }
    else
    {
        printf("¿numero de digitos a calcular?\n");
        do
        {
            scanf("%d", &rango);
        }
        while(rango < limit);
    }

    printf("fibonacci series: 0 1 ");

    for(int i = 0; i < rango - 2; i++)
    {
        c = a + b;
        a = b;
        b = c;
        printf("%d ", c);
    }
    printf("\n");
}
