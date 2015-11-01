#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 1: Binary Multiplication

Team Number: 
Student Names:
'''
import unittest
import math
def binary_mult(A,B):
    """
    Sig:    int[0..n-1], int[0..n-1] ==> int[0..2*n-1]
    Pre:    
    Post:   
    Var:    
    Example:    binary_mult([0,1,1],[1,0,0]) = [0,0,1,1,0,0]
    """
    #Y, X = make_input_same_length(A,B)
    maxlen = max(len(A), len(B))
    if maxlen == 1:
        return A[0]*B[0]
    else:
        p = []
        q = []
        r = []
        s = []

        for i in range(0, maxlen):
            if i <= maxlen/2:
                p.append(A[i])
                r.append(B[i])
            else:
                q.append(A[i])
                s.append(B[i])

        P1 = binary_mult(p,r)
        P2 = binary_mult(q,s)
        #z = add_binary(p,q)
       # w = add_binary(r,s)
        P3 = binary_mult(q,r)
        P4 = binary_mult(p,s)

        P3 = add_binary(P3,P4)
        P2 = P2 >> len(A)
        P3 = P3 >> len(A)/2

        P5 = add_binary(P2, P3)
        return add_binary(P5, P1)

#performs binary addition
def add_binary(X,Y):
        maxlen = max(len(X), len(Y))

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
    y = [1,0,1,0,0]
    #print make_input_same_length(a,y)
    #t, z = make_input_same_length(a,y)
    #print t
    #print z
    z = binary_mult(a,y)
    print z