#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import math
"""
Python 2.7 Katas (String Practice)

You will create a single file for all these exercises. 
Each individual exercise should print its result to the console. 

NOTE: follow this pattern in your file for ease of grading
and checking your own work:
print ' 1. ----------------------------'
# code for 1. goes here.
print ' 2. ----------------------------'
# code for 2. goes here

author: bobh "bomazani"
"""


print("""1. Create a method/function so that it converts dash/underscore delimited words 
into camel casing. The first word within the output should be capitalized 
only if the original word was capitalized.""")


def to_camel_case(string):
    split_string = string.replace('-', " ").replace('_', " ").split()
    new_list = [split_string[0]]
    split_list = split_string[1:]
    for item in split_list:
        new_list.append(item.capitalize())
    new_string = "".join(new_list)
    print(new_string)
    return


to_camel_case("the-stealth-warrior")
to_camel_case("I am not stealthy or a warrior")
to_camel_case("The_Stealth_Warrior")


print("""2. Implement a function find_nth_occurrence 
that returns the index of the nth occurrence of a substring within a string 
(considering that those substring could overlap each others). 
If there are less than n occurrences of the substring, return -1.""")


def find_nth_occurrence(n, sub, string):
    count = 0
    start = 0

    while count < n:
        index = string.find(sub, start=start)
        count += 1
        start = index + 1

    return index


print("answer: " + str(find_nth_occurrence(1, "TestTest", "TestTestTestTest")))
print("expect answer to be index: 0")
print("answer: " + str(find_nth_occurrence(2, "TestTest", "TestTestTestTest")))
print("expect answer to be index: 4")
print("answer: " + str(find_nth_occurrence(3, "TestTest", "TestTestTestTest")))
print("expect answer to be index: 8")
print("answer: " + str(find_nth_occurrence(4, "TestTest", "TestTestTestTest")))
print("expect answer to be index: -1")
print("answer: " + str(find_nth_occurrence(5,
                                           "TestTest", "TestTestTestTestTestTestTestTest")))
print("expect answer to be index: 16")

print('''3. Your beater car can\'t take another Indiana winter. 
The shock absorbers are gone and you think it can handle about 15 more potholes 
before it\'s wrecked. Unfortunately for you, your drive is very bumpy! 
Given a string showing either flat road ("_") or bumps ("n"), work out 
if you make it home safely. 15 bumps or under, return "Woohoo!", 
over 15 bumps return "Car Dead".''')

test1 = "_nnnnnnn_n__n______nn__nn_nnn"
test2 = "______n___n_"


def count_bumps(string):
    num_bumps = string.count('n')
    if num_bumps <= 15:
        print("Woohoo!")
    else:
        print("Car Dead")


count_bumps(test1)
count_bumps(test2)


print("""4. Complete the function that accepts a string parameter, 
and reverses each word in the string. 
All spaces in the string should be retained.""")

def reverse_indiv_words(string):
    word_list = string.split(" ")
    final_list = []
    for word in word_list:
        # word = word[::-1]
        final_list.append(word[::-1])
    new_string = ' '.join(final_list)
    return new_string

# *** refactored ***
# def reverse_words(sentence):
#     reversed_words = ' '.join(reversed(sentence.split(' ')))
#     print("reversed_words: {}.format(reversed_words))
#     return reversed_words[::-1]


reverse_indiv_words("This is an example!")
reverse_indiv_words("double  spaces")
