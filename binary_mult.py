#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Assignment 1: Binary Multiplication
Team Number: 2
Student Names: Alieu Jallow, Oceane Boetsch
"""
import unittest

def binary_mult(A, B):
    
    #Sig: int[0..n-1], int[0..n-1] ==> int[0..2*n-1]
    #Pre: A and B only contain 0 or 1, len(A)>0, len(B)>0
    #Post: A*B is of size n*2    
    #Example:    binary_mult([0,1,1],[1,0,0]) = [0,0,1,1,0,0]
    
    if len(A)<=0 and len(B)<=0:
        return []

    A, B = make_input_same_length(A,B)

    maxlen = max(len(A), len(B))
    n= maxlen / 2
    m = (maxlen + 1) / 2

    if maxlen == 1:
        result =  A[0] * B[0]
        return [0]+[result]

    #Divide each of A and B by half in subdigits 
    a_left = A[ : m]
    a_right = A[ m :]
    b_left = B[ : m]
    b_right = B[ m :]

    #First recursion, multiplication of the left half of A by the left half of B
    a_l_b_l = binary_mult(a_left, b_left)
    #Second recursion, multiplication of the right half of A by the right half of B
    a_r_b_r = binary_mult(a_right, b_right)
    #Third recursion, multiplication of the sum of the two halves of A by the sum of the two halves of b
    c = binary_mult(binary_add(a_left, a_right), binary_add(b_left, b_right))

    #Substraction of the result of the third recursion by the sum of the first and second recursion
    d = binary_subt(c, binary_add(a_l_b_l,  a_r_b_r))

    e = a_l_b_l + [0 for i in range(0, 2*n)]
    f = d + [0 for i in range(0, n)]

    result = binary_add(binary_add(e,  f), a_r_b_r)
    return result

#perform binary substraction
def binary_subt(x, y):
    x, y = make_input_same_length(x,y)
    maxlen = max(len(x), len(y))
    result = []

    for i in range(1,len(x)+1):
        #variant : i, diff, result
        diff = x[-i] - y[-i]

        if diff >= 0:
            result.append(diff)
        else:
            k = i + 1
            while k <= maxlen:
                #variant : k, x
                x[-k] = (x[-k] + (2 - 1)) % 2
                if x[-k] != 2 - 1:
                    break
                else:
                    k += 1
            result.append(diff + 2)
    result.reverse()
    return result

#Adjust the length of the inputs to same
def make_input_same_length(x,y):
    diff = 0
    z = []
    if len(x) > len(y):
        diff = len(x) - len(y)
        z = [0] * diff
        y = z+y
        return x,y
    else:
        diff = len(y) - len(x)
        z = [0] * diff
        x = z+x
        return x, y

#performs binary addition
def binary_add(x,y):
    #adjusts the inputs to have one length
    a, b= make_input_same_length(x,y)
    maxlen = max(len(x), len(y))

    carry =0
    result=[]

    for i in range(1, len(a)+1):
        #variant : i, val, result, carry
        val = a[-i] + b[-i] + carry
        result.append(val % 2)
        carry = val /2
    if carry !=0:
        result.append(carry)

    result.reverse()

    return result




class BinaryMultTest(unittest.TestCase):
    """Test Suite for binary multiplication problem
    Any method named "test_something" will be run when this file is 
    executed. Use the sanity check as a template for adding your own 
    tests if you wish. 
    (You may delete this class from your submitted solution.)
    """
    
    def test_sanity(self):
        """Sanity Test
        
        This is a simple sanity check for your function;
        passing is not a guarantee of correctness.
        """
        A = [0,1,1,0]
        B = [0,0,1,0]
        answer = binary_mult(A, B)
        self.assertEqual(answer, [0,0,0,0,1,1,0,0])

if __name__ == '__main__':

    #unittest.main()
    A = [0,1,1]
    B = [1,0,0,0]

    z = binary_mult(A,B)
    print z