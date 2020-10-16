"""
Author: Professor Cody Watson
Washington and Lee University
"""

"""
QUESTION
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
Example:
    Input: [1,2,3,4]
    Output:[24,12,8,6]
"""

def getProductList(lst):
    productList = []
    ans = 1
    for i in range(len(lst)):
        for j in range(len(lst)):
            if j != i:
                ans *= lst[j]
        productList.append(ans)
        ans = 1
    return productList


import functools
def getProductListDivision(lst):
    productList = []
    result = functools.reduce((lambda x, y: x*y), lst)
    for i in range(len(lst)):
        productList.append(result / lst[i])
    return productList


def getProductList_fast(lst):
        length = len(lst)
        Left = [0]*length
        Right = [0]*length
        final = [0]*length
        Left[0] = 1
        for i in range(1, length):
            Left[i] = lst[i - 1] * Left[i - 1]
        Right[length - 1] = 1
        for i in reversed(range(length - 1)):
            Right[i] = lst[i + 1] * Right[i + 1]
        for i in range(length):
            final[i] = Left[i] * Right[i]       
        return final    