'''
Given an array arr[] of size N, check if it can be partitioned into
two parts such that the sum of elements in both parts is the same.

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

def solution(arr):
    return True

if __name__ == "__main__":
    print("\nTest begins...\n")

    # ~ADD TEST CASE HERE~
    # test case arg format: (arg1, arg2, ..., correct_out)
    test_cases = [
        [[1, 5, 11, 5], True],
        [[1, 3, 5], False]
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