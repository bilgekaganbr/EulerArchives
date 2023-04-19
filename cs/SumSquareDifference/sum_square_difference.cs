namespace sum_square_difference
{
    class sum_square_difference
    {
        static void Main(string[] args)
        {
            /*Program that calculates the difference between the sum of the squares of the first ten natural numbers and the square
            of the sum of the first ten natural numbers*/

            //Initialize sums from 0
            int sum1 = 0;
            int sum2 = 0;

            //Sum1 is the sum of the squares of the first ten natural numbers and sum2 is the sum of first ten natural numbers
            for(int i = 1; i <= 100; i++)
            {
                sum1 += (int)Math.Pow(i, 2);
                sum2 += i;
            }

            //Calculate difference by using the square of sum2 and sum1
            int diff = (int)Math.Pow(sum2, 2) - sum1;
            Console.WriteLine(diff);
        }
    }
}
