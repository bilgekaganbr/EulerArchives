#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    /*Program that calculates the difference between the sum of the squares of the first ten natural numbers and the square
    of the sum of the first ten natural numbers*/

    //Initialize sums from 0
    int sum1 = 0;
    int sum2 = 0;

    //Sum1 is the sum of the squares of the first ten natural numbers and sum2 is the sum of first ten natural numbers
    for (int i = 1; i <= 100; i++)
    {
        sum1 += (int)pow(i, 2);
        sum2 += i;
    }

    //Calculate difference by using the square of sum2 and sum1
    int diff = (int)pow(sum2, 2) - sum1;
    printf("%i\n", diff);
}