# Andres_Leon
# cod: 624503
# Taller ordenamiento con recurrencias 
# Codigo en python con varios algoritmos de ordenamiento
# usa @print_timing

import random  # genera numeros aleatorios
import time    # para medir el tiempo con la funcion time.clock()
DEBUG = False  # set True to check results of each sort
N = 1000     # numero de elementos en la lista, se probara con 10, 100, 200
list1 = []   # lista de numeros sera de enteros

for i in range(0, N):
    list1.append(random.randint(0, N-1))
#print list1  # test
def print_timing(func):
    def wrapper(*arg):
        t1 = time.clock()
        res = func(*arg)
        t2 = time.clock()
        print '%s took %0.3fms' % (func.func_name, (t2-t1)*1000.0)
        return res
    return wrapper
# declare the @ decorator just above each sort function, invokes print_timing()
#################################################Heap Sort Implementation##############################################
@print_timing

def heap_sort(list2):
    first = 0
    last = len(list2) - 1
    create_heap(list2, first, last)
    for i in range(last, first, -1):
        list2[i], list2[first] = list2[first], list2[i]  # swap
        establish_heap_property (list2, first, i - 1)
		
# create heap (used by heap_sort)
def create_heap(list2, first, last):
    i = last/2
    while i >= first:
        establish_heap_property(list2, i, last)
        i -= 1
		
# establish heap property (used by create_heap)
def establish_heap_property(list2, first, last):
    while 2 * first + 1 <= last:
        k = 2 * first + 1
        if k < last and list2[k] < list2[k + 1]:
            k += 1
        if list2[first] >= list2[k]:
            break
        list2[first], list2[k] = list2[k], list2[first]  # swap
        first = k
		
#################################################QuickSort Implementation##############################################		
@print_timing
def quick_sort(list2):
    quick_sort_r(list2, 0, len(list2) - 1)
# quick_sort_r, recursive (used by quick_sort)
def quick_sort_r(list2 , first, last):
    if last > first:
        pivot = partition(list2, first, last)
        quick_sort_r(list2, first, pivot - 1)
        quick_sort_r(list2, pivot + 1, last)
# partition (used by quick_sort_r)
def partition(list2, first, last):
    sred = (first + last)/2
    if list2[first] > list2 [sred]:
        list2[first], list2[sred] = list2[sred], list2[first]  # swap
    if list2[first] > list2 [last]:
        list2[first], list2[last] = list2[last], list2[first]  # swap
    if list2[sred] > list2[last]:
        list2[sred], list2[last] = list2[last], list2[sred]    # swap
    list2 [sred], list2 [first] = list2[first], list2[sred]    # swap
    pivot = first
    i = first + 1
    j = last
  
    while True:
        while i <= last and list2[i] <= list2[pivot]:
            i += 1
        while j >= first and list2[j] > list2[pivot]:
            j -= 1
        if i >= j:
            break
        else:
            list2[i], list2[j] = list2[j], list2[i]  # swap
    list2[j], list2[pivot] = list2[pivot], list2[j]  # swap
    return j
		
##########################################################CountingSort######################################################
def counting_sort(list2, maxval):
    """in-place counting sort"""
    m = maxval + 1
    count = [0] * m               # init with zeros
    for a in list2:
        count[a] += 1             # count occurences
    i = 0
    for a in range(m):            # emit
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            list2[i] = a
            i += 1
    return list2
 
print counting_sort( [1, 4, 7, 2, 1, 3, 2, 1, 4, 2, 3, 2, 1], 7 )
#            prints: [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 7]

##########################################################RadixSort######################################################
# Radix sort for fixed length strings
def radixSortFixedString(list2):
    fixedLength = len(list2[0])
    oa = ord('a'); # First character code
    oz = ord('z'); # Last character code
    n = oz - oa + 1; # Number of buckets
    buckets = [[] for i in range(0, n)] # The buckets
    for position in reversed(range(0, fixedLength)):
        for string in list2:
            buckets[ord(string[position]) - oa].append(string) # Add to bucket
	        del list2[:]
	        for bucket in buckets: # Reassemble list2 in new order
            list2.extend(bucket)
            del bucket[:]
return list2


##testing lists
# test sorted list by printing the first 10 elements
def print10(list2):
    for k in range(10):
        print list2[k],
    print
# run test if script is executed
if __name__ == "__main__" :
    print "timing 7 sorting algorithms with a list of 1000 integers:"
    # make a true copy of list1 each time
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    heap_sort(list2)
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    quick_sort(list2)
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    counting_sort(list2)
	if DEBUG:
        print10(list2)
    list2 = list(list1)
    radixSortFixedString(list2)
    if DEBUG:
        print10(list2)
    # final test
    list2 = list(list1)
    if DEBUG:
        print "final test: ",
        print10(list2)
    #raw_input( "Press Enter to continue..." )
	
#
#typical results:
#timing sorting algorithms with a list of 1000 integers:
#heap_sort took 13.556ms
#quick_sort took 6.849ms


# Bibliografia:
# [1] from http://www.daniweb.com/software-development/python/code/216689/sorting-algorithms-in-python#
# [2] from http://codehost.wordpress.com/2011/07/22/radix-sort/