#!/usr/bin/env python
# coding=utf-8

numbers = [5,23,4,56,2,33,45,25]
even = []
odd = []
while len(numbers) > 0 :
    number = numbers.pop()
    if(number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)

print "even:",even
print "odd:",odd