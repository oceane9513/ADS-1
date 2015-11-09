#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

#Assignment 1: Integer Sort

#Team Number: 2
#Student Names: Alieu Jallow, Oceane Boetsch

import unittest

def integer_sort(A, k):
    
    #Sig: int array[1..n], int -> int array[1..n]
    #Pre: k > max(A[0...n-1])
    #Post: A is a non-decreasing sequence of integers
    #Example: integer_sort([5, 3, 6, 7, 12, 3, 6, 1, 4, 7]), 12) = [1, 3, 3, 4, 5, 6, 6, 7, 7, 12]
    
    #k is bigger or equal to all elements of A, A will be sorted
    if is_max_of_A(A,k):
        #Initialization at 0 of all the elements of Y
        Y = [0] * (k+1)
        #Fill the array Y : count for i in [0,n], the number of i in A
        for i in range(0,len(A)):
            #variant : i, Y[A[i]]
            Y[A[i]] +=1
        index = 0
        #Rewrite the array A in the order
        for j in range(0,k+1):
            #variant : j
            for  s in range(0,Y[j]):
                #variant : s, A[index], index
                A[index] = j
                index += 1
        #Return the sorted array
        return A

    #k is not bigger or equal to all elements of A, A can't be sorted
    else :
        return False

def is_max_of_A(A,k):
    is_max = False
    #Check if every element of A are smaller than k
    for i in range(0,len(A)):
        #variant : i
        if A[i] > k:
            return False
        else:
            is_max = True
    return is_max

class IntegerSortTest(unittest.TestCase):
    #Test Suite for integer sort problem
    
    
    def test_sanity(self):
        
        #This is a simple sanity check for your function; passing is not a guarantee of correctness.
        
        A = [5, 3, 6, 7, 12, 3, 6, 1, 4, 7]
        B=integer_sort(A, 13)
        if B==False:
            print 'k is not bigger than all the element of A'
        else:
            self.assertEqual(A, [1, 3, 3, 4, 5, 6, 6, 7, 7, 12])


if __name__ == '__main__':
    unittest.main()