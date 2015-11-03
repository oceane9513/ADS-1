#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 1: Birthday Present

Team Number: 2
Student Names: Alieu Jallow,
'''
import unittest

def birthday_present(P, n, t):
    '''

    Resursive equation: birthday_present(P, n, t) = birthday_present(P, n-1, t) ||
                           birthday_present(P, n-1, t - P[n-1])

    Base Cases:
    birthday_present(P, n, t) = false, if t > 0 and n == 0
    birthday_present(P, n, t) = true, if t == 0

    Sig: int[0..n-1], int, int --> Boolean
    Pre:
    Post:
    Example: P = [2, 32, 234, 35, 12332, 1, 7, 56]
             birthday_present(P, len(P), 299) = True
             birthday_present(P, len(P), 11) = False
    '''
    # Initialize the dynamic programming matrix, A
    # Type: Boolean[0..n][0..t]
    A = [[None for i in range(t + 1)] for j in range(n + 1)]
    #A[n+1][t+1]

    #initialise the matrix A with True if t = 0
    for i in range(0, n+1):
        A[i][0] = True
    #initialise the matrix A with False if P is empty and t not equal to 0
    for i in range(1, t+1):
        # invariant: i <= t
        A[0][i] = False

    # Fill the matrix A in a bottom up matter
    for i in range(1,n+1):
        #invariant:
        # variant:
         for j in range(1,t+1):
             #invariant:
            # variant:
             #get the values from the top
             A[i][j] = A[i-1][j]

             if j >= P[i-1]:
                 A[i][j] = A[i][j] or A[i-1][j-P[i-1]]

    return A[n][t]

def birthday_present_subset(P, n, t):
    '''
    Sig: int[0..n-1], int, int --> int[0..m]
    Pre: 
    Post: 
    Example: P = [2, 32, 234, 35, 12332, 1, 7, 56]
             birthday_present_subset(P, len(P), 299) = [56, 7, 234, 2]
             birthday_present_subset(P, len(P), 11) = []
    '''
    A = [[None for i in range(t + 1)] for j in range(n + 1)]
    Q = []
    #initialise the matrix A with True if t = 0
    for i in range(0, n+1):
        A[i][0] = True
    #initialise the matrix A with False if P is empty and t not equal to 0
    for i in range(1, t+1):
        # invariant: i <= t
        A[0][i] = False

    # Fill the matrix A in a bottom up matter
    for i in range(1,n+1):
        #invariant:
        # variant:
         for j in range(1,t+1):
            #invariant:
            #variant:
            #get the values from the top
             A[i][j] = A[i-1][j]

             if j >= P[i-1]:
                 A[i][j] = A[i][j] or A[i-1][j-P[i-1]]

    #checks if there exists a subset, then returns an empty list
    if A[n][t]==False:
        return Q
    #There exists a subset, then start from the bottom right corner
    #and trace back where True is coming from
    else:
        j = t
        i = n
        #variants: i and j
        while j != 0:
            if A[i][j] == True and A[i-1][j] == False:
                Q.append(P[i-1])
                j = j-P[i-1]
            else:
                i = i - 1
    return Q




class BirthdayPresentTest(unittest.TestCase):
    """Test Suite for birthday present problem
    
    Any method named "test_something" will be run when this file is 
    executed. Use the sanity check as a template for adding your own 
    tests if you wish. 
    (You may delete this class from your submitted solution.)
    """
    
    def test_sat_sanity(self):
        """Sanity Test for birthday_present()
        
        This is a simple sanity check;
        passing is not a guarantee of correctness.
        """
        P = [2, 32, 234, 35, 12332, 1, 7, 56]
        n = len(P)
        t = 11
        self.assertFalse(birthday_present(P, n, t))
    def test_sol_sanity(self):
        """Sanity Test for birthday_present_subset()
        
        This is a simple sanity check;
        passing is not a guarantee of correctness.
        """
        P = [2, 32, 234, 35, 12332, 1, 7, 56]
        n = len(P)
        t = 299
        self.assertTrue(birthday_present(P, n, t))
        self.assertItemsEqual(birthday_present_subset(P, n, t), 
                              [56, 7, 234, 2])
        
if __name__ == '__main__':
    #unittest.main()

    P = [5, 2, 6, 1, 7]
    n = len(P)
    t = 21

    q = birthday_present_subset(P, n, t)
    print q
