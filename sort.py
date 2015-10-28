# For compatability between Python versions 2.x and 3.x
from __future__ import print_function

import os
import array
import sys
import time
import math

# Bubble Sort Implementation

def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t

def bubblesort(a):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                swap(a, i, i+1)
                sorted = False



# Implementation of InsertionSort
def insertionSort(a):

    for j in range(1,len(a)):
        key = a[j]
        i = j
        while (i>0 and a[i-1]>key):
            a[i]= a[i-1]
            i = i-1
        if(i!=j):
            a[i]= key

#implementation of QuickSort
def partition(array, p, r):
    x = array[r]
    i=p-1
    for j in range(p,r):
         if array[j] <= x:
            i =i+1
            swap(array,i,j)
    swap(array, i+1 , r)
    return i+1

def quickSort(array, p, r):
    if p<r:
        q = partition(array,p,r)
        quickSort(array,p,q-1)
        quickSort(array,q+1,r)

#heap sort implementations
def Left(i):
    return 2*i+1

def Right(i):
    return (2*i)+2

#implementation of MAX-HEAPIFY
def max_heapify(A, i, heap_size):
    l= Left(i)
    r=Right(i)
    if l<=heap_size-1 and A[l]>A[i]:
        largest = l
    else:
        largest = i
    if r<=heap_size-1 and A[r]> A[largest]:
        largest =r
    if largest!=i:
        swap(A,i,largest)
        max_heapify(A,largest, heap_size)

#implementation of BUILD-MAX-HEAP
def build_max_heap(A):
    heap_size = len(A)
    i = (len(A)/2)
    while i >=0:
        max_heapify(A,i,heap_size)
        i = i-1
#implementation of the HEAP Sort
def heapSort(A):
    build_max_heap(A)
    heap_size =len(A)
    i = len(A)-1
    while i>0:
        swap(A,0,i)
        heap_size = heap_size -1
        max_heapify(A, 0, heap_size)
        i=i-1

# This is the function to verify your implemented sorting algorithm
# You need to change it a bit to call your sorting algorithm
def test():
    # check if nums.txt exists
    if not os.path.exists('nums.txt'):
        print("First create nums.txt")
        sys.exit(0)

    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []

    for line in nums:
       a.append(int(str.strip(line)))

    # sort the array using your sorting algorithm implementation
    #build_max_heap(a)
    heapSort(a)
    insertionSort(a)
    quickSort(a,0,(len(a)-1))
    # output nums_sorted.txt
    nums_sorted = open('nums_sorted.txt', 'w')
    for element in a:
       nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()
    # compare your result (nums_sorted.txt) against the result of the unix/linux sorting algorithm (nums_ref.txt)
    os.system('sort -n nums.txt > nums_ref.txt')
    ret = os.system('diff nums_sorted.txt nums_ref.txt > tmp.txt')

    # Check output differences and output result
    if int(ret) == 0:
        print("Sorted!")

    if int(ret) != 0:
        print("Not sorted!")

# python sort.py runs test
if __name__ == "__main__":
    test()
