#include <stdio.h>

int f( int i, float f )
{
    i = i + 1;
    f = f + 1.0f;
    printf( "c(int,float): %d %f\n", i, f);
    return i;
}
