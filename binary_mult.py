#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 1: Binary Multiplication

Team Number: 
Student Names:
'''
import sys
#sys.setrecursionlimit(10000)
import unittest
import math
def binary_mult(A , B):
    """
    Sig: int[0..n-1], int[0..n-1] ==> int[0..2*n-1]
    Pre:    
    Post:   
    Var:    
    Example:    binary_mult([0,1,1],[1,0,0]) = [0,0,1,1,0,0]
    """
    #Y, X = make_input_same_length(A,B)
    #A· B = pr · 2^n + (ps + rq)· 2^n/2 + qs
    #assert len(A) > 0 and len(B)>0

    maxlen = max(len(A), len(B))
    if maxlen <= 1:
        return A[0] * B[0]
        #return [result] if result < 2 else [result / 2, result % 2]
    else:
        n = (maxlen + 1) / 2
        m= maxlen / 2

        p = A[:n]
        q = A[n:]
        r = B[:n]
        s = B[n:]

        P1 = binary_mult(p,r)
        P2 = binary_mult(q,s)
        P3 = binary_mult(binary_add(p, q), binary_add(r,s))

        P6 = binary_sub(P3, binary_add(P1,  P2))

        P8 = P1 + [0 for i in range(0, 2 * m)]
        P9 = P6 + [0 for i in range(0, m)]

        return binary_add( binary_add(P8, P9), P2)

#perform binary substraction
#Assumes all input is binary otherwise it returns error
def binary_sub(x, y):
    maxlen = max(len(x), len(y))
    x, y = make_input_same_length(x,y)
    result =[]

    for i in range(1,len(x)+1):
        diff = x[-i] - y[-i]

        if diff >=0:
            result.append(diff)
        else:
            k = i + 1
            while k<= maxlen:
                x[-k] = (x[-k] + (2 - 1)) % 2
                if x[-k] != 2 - 1:
                    break
                else:
                    k += 1
            result.append(diff+2)
    result.reverse()
    return result

#performs binary addition
def binary_add(x,y):
    maxlen = max(len(x), len(y))
    a, b= make_input_same_length(x,y)

    carry =0
    result=[]

    for i in range(1, len(a)+1):
        val = a[-i] + b[-i] + carry
        result.append(val % 2)
        carry = val /2
    if carry !=0:
        result.append(carry)

    result.reverse()
    return result

def add(X,Y):

        maxlen = max(len(X), len(Y))
        X, Y = make_input_same_length(X,Y)

        result = []
        for t in range(0, maxlen+1):
            result.append(0)

        for i in range(maxlen-1, -1, -1):
            if X[i]+Y[i]+result[i+1]==0:
                 result[i+1]=0
            elif X[i]+Y[i]+result[i+1]==1:
                result[i+1]=1

            elif X[i]+Y[i]+result[i+1]==2:
                result[i+1]=0
                result[i]=1
            else:
                result[i+1]=1
                result[i]=1
        return result

def make_input_same_length(x,y):
    diff =0
    z = []
    if len(x)> len(y):
        diff = len(x) - len(y)
        z = [0] * diff
        y = z+y
        return x,y
    else:
        diff = len(y) - len(x)
        z = [0] * diff
        x = z+x
        return x, y


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
   # unittest.main()
    a = [1,1,1,0,0]
    b = [1,0,1,0,0]
    #print make_input_same_length(a,y)
    #t, z = make_input_same_length(a,y)
    #print t
    #print z
    z = binary_mult(a,b)
    print z