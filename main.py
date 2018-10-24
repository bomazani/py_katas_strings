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


to_camel_case("the-stealth-warrior")
to_camel_case("I am not stealthy or a warrior")
to_camel_case("The_Stealth_Warrior")


print("""2. Implement a function find_nth_occurrence 
that returns the index of the nth occurrence of a substring within a string 
(considering that those substring could overlap each others). 
If there are less than n occurrences of the substring, return -1.""")
# find 'TestTest' in 'TestTestTestTest'. Find 1st,2nd,3rd,4th occurrences.
# def find_nth_occurrence(number:)
# sample = "TestTestTestTest"
# term = "TestTest"


def find_nth_occurrence(n, sub, string):
    occurrences = 0
    sub_len = len(sub)
    for letter in string:
        print(letter)
        print("index: " + str(string.index(letter)))
        start = string.index(letter)
        end = start + sub_len
        sample = string[start:end]
        print("sample: " + sample)
        if sample == sub:
            occurrences += 1
            print("occurrences: " + str(occurrences))
            print("n = " + str(n))
            print("index: " + str(start))
            if occurrences == n:
                answer = string.index(letter)
    print(answer)


find_nth_occurrence(2, "TestTest", "TestTestTestTest")

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
        word = word[::-1]
        final_list.append(word)
    new_string = ' '.join(final_list)
    print(new_string)


reverse_indiv_words("This is an example!")

reverse_indiv_words("double  spaces")
