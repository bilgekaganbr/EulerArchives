#Program that finds 10001st prime number

#Starting values
num = 4
i = 2
j = 2

while num > i:

    #If num can be divided by i, the num is not prime, then go to next num and reset i
    if num % i == 0:

        num += 1
        i = 2

    else:

        #If i equals to num - 1, then num is prime. Increase j by 1
        if i == num - 1:

            j += 1

            #If j is 10001, then print the num and end the loop
            if j == 10001:

                print(num)
                break

            #Else, go to next num and reset i
            num += 1
            i = 2

        #Else, go to next i
        else:

            i += 1














