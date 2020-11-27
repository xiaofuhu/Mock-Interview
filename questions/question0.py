'''
Write a short function to get K elements of a list such that
1. Each element is exactly T elements apart from its neighbors
2. The K elements are the first K elements satisfying requirement 1
3. Include any sanity checks as necessary
4. If no such K elements exist, return an empty array

Input:   arr = [1, 2, 3, 4, 5, 6, 7, 8],  K = 3, T = 1
Output:  [1, 3, 5]

Input:   arr = [1, 2, 3, 4, 5, 6, 7, 8],  K = 2, T = 3
Output:  [1, 5]
'''
import time

def solution(arr, K, T):
    return []

if __name__ == "__main__":
    print("\nTest begins...\n")

    # ~ADD TEST CASE HERE~
    # test case arg format: (arg1, arg2, ..., correct_out)
    test_cases = [
        [[1, 2, 3, 4, 5, 6, 7, 8], 3, 1, [1, 3, 5]],
        [[1, 2, 3, 4, 5, 6, 7, 8], 2, 3, [1, 5]]
    ]

    correct = 0
    current = 0
    for t in test_cases:
        print("Test {}:".format(current))
        t1 = time.time()
        ans = solution(t[0], t[1], t[2])
        duration = time.time() - t1
        if ans != t[3]:
            def error(got, correct):
                print("\tERROR: Got {}. Should be {}".format(got, correct))
            error(ans, t[3])
        else:
            correct += 1
            print("\tPASSED\tTook {:.4f} ms".format(duration))
        current += 1
    print("\n{} of {} correct\n".format(correct, len(test_cases)))