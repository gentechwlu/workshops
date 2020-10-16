"""
Author: Professor Cody Watson
Washington and Lee University
"""

"""
QUESTION
Given an array of integers, find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers.
Example: 
    Input: [3,5,6,2,3,4,5]
    Output: 5
"""

def longestSequence(lst):
    lst.sort()
    longest_run = 0
    for i in range(len(lst)):
        start = lst[i]
        end = start
        run = 0
        for j in range(i,len(lst)):
            if lst[j] == end + 1:
                run += 1
                end = lst[j]
            if run > longest_run:
                longest_run = run
    return longest_run + 1


def longestSequence_fast(lst):
    lst_set = set(lst)
    longest_run = 0
    for element in lst:
        #THIS IS THE KEY
        if element - 1 not in lst_set:
            current_element = element
            current_run = 1
            while current_element + 1 in lst_set:
                current_element += 1
                current_run += 1
            if current_run > longest_run:
                longest_run = current_run
    return longest_run