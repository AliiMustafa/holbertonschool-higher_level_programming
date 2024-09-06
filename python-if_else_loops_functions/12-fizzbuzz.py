#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        div3 = i % 3 == 0
        div5 = i % 5 == 0
        if div3 and div5:
            print("FizzBuzz", end=" ")
        elif div3:
            print("Fizz", end=" ")
        elif div5:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
