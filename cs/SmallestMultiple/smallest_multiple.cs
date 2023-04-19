namespace smallest_multiple
{
    class smallest_multiple
    {
        static void Main(string[] args)
        {
            //Program that calculate the smallest number which can be evenly divided by numbers from 1 to 20

            //Initialize i and number from 1
            int i = 1;
            int number = 1;

            while (i <= 20)
            {
                //If number can be divided by i, increase i by 1 and do not change the number
                if (number % i == 0)
                {
                    i++;
                }
                //Else, reset i and increase number by 1
                else
                {
                    i = 1;
                    number++;
                }
            }

            Console.WriteLine(number);
        }
    }
}