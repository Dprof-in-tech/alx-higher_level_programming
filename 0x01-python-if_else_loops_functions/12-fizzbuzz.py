#!/usr/bin/python3
"""function should print numbers 1 - 100 seperated by a space
    for number multiples of 3, print Fizz instead of the number
    for number multiples of 5 , print buzz"""
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('{} '.format('FizzBuzz'), end='')
        elif i % 3 == 0:
            print('{} '.format('Fizz'), end='')
        elif i % 5 == 0:
            print('{} '.format('Buzz'), end='')
        else:
            print('{} '.format(i), end='')

fizzbuzz()
