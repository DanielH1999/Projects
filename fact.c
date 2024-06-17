#include<stdlib.h>
#include<stdio.h>

//definir variable
int input;

//funcion que pide el valor de input
void noargs(void)
{
    printf("factorial de...\n");
    scanf("%d", &input);
}


void main(int argc, char* argv[])
{
    int fact = 1;

    //si no hay argumentos de CLI, pedi valor de input
    if(argc != 2)
    {
        noargs();
    }
    //en caso de que haya un argumento, transformar de string a int y asignar a input
    else
    {
        input = atoi(argv[argc - 1]);
    }
    //iterar en input y operar factorial
    for(int i = input; i > 0; i--)
    {
        fact *= i;
    }
    //imprimir factorial
    printf("%d\n", fact);
}
