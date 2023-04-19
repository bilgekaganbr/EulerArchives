#Program that calculates the difference between the sum of the squares of the first ten natural numbers and the square
#of the sum of the first ten natural numbers

#Initialize sums from 0
sum1 = 0
sum2 = 0

for i in range(1,101):

    #Sum1 is the sum of the squares of the first ten natural numbers and sum2 is the sum of first ten natural numbers
    sum1 += i**2
    sum2 += i

#Calculate difference by using the square of sum2 and sum1
diff = sum2**2 - sum1
print(diff)