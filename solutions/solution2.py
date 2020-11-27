'''
Given an array arr[] of size N, check if it can be partitioned into
two parts such that the sum of elements in both parts is the same.
All the elements in arr are guaranteed to be integers.

Input: N = 4
arr = {1, 5, 11, 5}
Output: YES
Explaination: 
The two parts are {1, 5, 5} and {11}.

Input: N = 3
arr = {1, 3, 5}
Output: NO
Explaination: This array can never be 
partitioned into two such parts.
'''
import time

def rec(arr, target):
    # No action needed to sum up to 0
    if target == 0:
        return True
    # Impossible to sum up to any non-zero value
    if len(arr) == 0:
        return False
    # Consider first element taken or not taken
    return rec(arr[1:], target - arr[0]) or rec(arr[1:], target)

def solution(arr):
    target = sum(arr) / 2.0
    # Integers cannot sum up to fractions
    if not int(target) == target:
        return False
    return rec(arr, target)

if __name__ == "__main__":
    print("\nTest begins...\n")

    # ~ADD TEST CASE HERE~
    # test case arg format: (arg1, arg2, ..., correct_out)
    test_cases = [
        [[1, 5, 11, 5], True],
        [[1, 3, 5], False],
        [[0, 0, 0, 0], True],
        [[], True],
        [[1, 2, 3, 4, 5, 6], False],
        [[1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7], True],
        [[1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, \
          4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, \
          7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, \
          3, 4, 5, 6, 7], True],
        [[2, 3, 5, 7, 11, 13, 17], True],
        [[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 500], False],
        [[-1, -999, 1000, 0], True],
        [[-1, -999, 1000, 2], True],
        [[-1, -999, 1001, 2], False],
    ]

    correct = 0
    current = 0
    for t in test_cases:
        print("Test {}:".format(current))
        t1 = time.time()
        ans = solution(t[0])
        duration = time.time() - t1
        if ans != t[1]:
            def error(got, correct):
                print("\tERROR: Got {}. Should be {}".format(got, correct))
            error(ans, t[1])
        else:
            correct += 1
            print("\tPASSED\tTook {:.4f} ms".format(duration))
        current += 1
    print("\n{} of {} correct\n".format(correct, len(test_cases)))