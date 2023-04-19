#Program that calculate the smallest number which can be evenly divided by numbers from 1 to 20

#Initialize i and number from 1
i = 1
number = 1

while i <= 20:

    #If number can be divided by i, increase i by 1 and do not change the number
    if number % i == 0:

        i += 1

    #Else, reset i and increase number by 1
    else:

        i = 1
        number += 1

print(number)
