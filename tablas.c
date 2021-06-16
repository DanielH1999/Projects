#include<stdio.h>
#include<stdlib.h>

int number;

//IF THERE IS NO ARGS GIVEN, ASK WHAT NUMBER THE USER WANTS
void noargs(void)
{
	printf("¿que tabla queres?...\n");
	scanf("%d", &number);
}

//MAIN FUNCTION

void main(int argc, char* argv[])
{

	if(argc != 2)
	{
		printf("tambien podes usar este programa como \"./tablas n\"\n");
		noargs();
	}
	else
	{
		number = atoi(argv[argc - 1]);
	}

	for(int i = 1; i <= 10; i++)
	{
		printf("%d * %d = %d\n", number, i, number * i);
	}
}
