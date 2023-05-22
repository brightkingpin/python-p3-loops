#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")


def square_integers(int_list):
    squared_list = []
    for num in int_list:
        squared_list.append(num ** 2)
    return squared_list
# Example
#print(square_integers([1, 2, 3, 4, 5]))
# Output: [1, 4, 9, 16, 25]



def fizzbuzz():
    for num in range(1, 101):  # Iterate from 1 to 100 (inclusive)
        if num % 3 == 0 and num % 5 == 0:  # Check if the number is divisible by both 3 and 5
            print("FizzBuzz")  # If so, print "FizzBuzz"
        elif num % 3 == 0:  # Check if the number is divisible by 3
            print("Fizz")  # If so, print "Fizz"
        elif num % 5 == 0:  # Check if the number is divisible by 5
            print("Buzz")  # If so, print "Buzz"
        else:
            print(num)  # If none of the above conditions are met, print the number itself


