#Task No 2(C)
num_1 = int (input ("Enter the first number: "))
num_2 = int (input ("Enter the second number: "))
num_3 = int (input ("Enter the third number: "))

if num_1 > num_2 and num_1 > num_3:
    print ("The first number is the largest")
elif num_2 > num_1 and num_2 > num_3:
    print ("The second number is the largest")
elif num_3 > num_1 and num_3 > num_2:
    print ("The third number is the largest")
else:
    print ("The numbers are equal")