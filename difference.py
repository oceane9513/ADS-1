#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 2: Search String Replacement

Team Number: 
Student Names: 
'''
import unittest
# Sample matrix provided by us:
from string import ascii_lowercase

# Solution to part b:
def difference(u,r,R):
    """
    Sig:    string, string, int[0..|A|, 0..|A|] ==> int
    Pre:    
    Post:    
    Example: difference("dynamic","dinamck",R) ==> 3
    """
    # To get the resemblance between two letters, use code like this:
    # difference = R['a']['b']
    
# Solution to part c:
def difference_align(u,r,R):
    """
    Sig:    string, string, int[0..|A|, 0..|A|] ==> int, string, string
    Pre:    
    Post:    
    Example: difference_align("dynamic","dinamck",R) ==> 
                                    3, "dynamic-", "dinam-ck"
    """

def qwerty_distance():
    """Generates a QWERTY Manhattan distance resemblance matrix
    
    Costs for letter pairs are based on the Manhattan distance of the
    corresponding keys on a standard QWERTY keyboard.
    Costs for skipping a character depends on its placement on the keyboard:
    adding a character has a higher cost for keys on the outer edges,
    deleting a character has a higher cost for keys near the middle.
    
    Usage:
        R = qwerty_distance()
        R['a']['b]  # result: 5
    """
    R = defaultdict(dict)
    R['-']['-'] = 0
    zones = ["dfghjk", "ertyuislcvbnm", "qwazxpo"]
    keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    for num, content in enumerate(zones):
        for char in content:
            R['-'][char] = num + 1
            R[char]['-'] = 3 - num
    for a in ascii_lowercase:
        rowA = None
        posA = None
        for num, content in enumerate(keyboard):
            if a in content:
                rowA = num
                posA = content.index(a)
        for b in ascii_lowercase:
            for rowB, contentB in enumerate(keyboard):
                if b in contentB:
                    R[a][b] = math.fabs(rowB - rowA) + math.fabs(posA - contentB.index(b))
    return R
    
class DifferenceTest(unittest.TestCase):
    """Test Suite for search string replacement problem
    
    Any method named "test_something" will be run when this file is
    executed. Use the sanity check as a template for adding your own test
    cases if you wish. 
    (You may delete this class from your submitted solution.)
    """

    def test_diff_sanity(self):
        """Difference sanity test
        
        Given a simple resemblance matrix, test that the reported 
        difference is the expected minimum. Do NOT assume we will always
        use this resemblance matrix when testing!
        """
        alphabet = ascii_lowercase + '-'
        # The simplest (reasonable) resemblance matrix: 
        R = dict( [ (
                     a,
                     dict( [ ( b, (0 if a==b else 1) ) for b in alphabet ] ) 
                    ) for a in alphabet ] )
        # Warning: we may (read: 'will') use another matrix!
        self.assertEqual(difference("dynamic","dinamck",R),3)
    def test_align_sanity(self):
        """Simple alignment
        
        Passes if the returned alignment matches the expected one.
        """
        alphabet = ascii_lowercase + '-'
        R = dict( [ (
                      a, 
                      dict( [ ( b, (0 if a==b else 1) ) for b in alphabet ] )
                    ) for a in alphabet ] )
        diff, u, r = difference_align("polynomial", "exponential", R)
        self.assertEqual(diff, 6)
        self.assertEqual(u,'--polynomial')
        self.assertEqual(r, 'exponen-tial')
if __name__ == '__main__':
    unittest.main()
