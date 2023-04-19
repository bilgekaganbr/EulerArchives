#include <stdio.h>
#include <cs50.h>

//Program that calculate the smallest number which can be evenly divided by numbers from 1 to 20

int main(void)
{

    int i = 1;
    int number = 1;

    while (i <= 20)
    {
        if (number % i == 0)
        {
            i++;
        }
        else
        {
            i = 1;
            number++;
        }
    }
    printf("%i\n", number);
}
