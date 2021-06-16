#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    int inp, n, see, res = 0;

    if(argc > 1)
    {
        inp = atoi(argv[argc-1]);
    }
    else
    {
        printf("numero: ");
        scanf("%d", &inp);
    }

    n = inp;

    while (n > 0) {
        see = n % 10;
        n /= 10;
        res += see;
    }
    printf("resultado: %d\n", res);
    return 0;
}
