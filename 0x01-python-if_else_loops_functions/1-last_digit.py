#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = abs(number) % 10 * -1
else:
    last_digit = number % 10
words = 'Last digit of {} is {}'.format(number, last_digit)
if (last_digit > 5):
    print('{} and is greater than 5'.format(words))
elif (last_digit == 0):
    print('{} and is 0'.format(words))
elif (last_digit < 6 and last_digit != 0):
    print('{} and is less than 6 and not 0'.format(words))
