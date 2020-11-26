'''
Given two strings str1 and str2, the task is to find the length
of the shortest string that has both str1 and str2 as subsequences.

Input:   str1 = "geek",  str2 = "eke"
Output: 5
Explanation: 
String "geeke" has both string "geek" 
and "eke" as subsequences.

Input:   str1 = "AGGTAB",  str2 = "GXTXAYB"
Output:  9
Explanation: 
String "AGXGTXAYB" has both string 
"AGGTAB" and "GXTXAYB" as subsequences.
'''

def solution(str1, str2):
    return(-1)

if __name__ == "__main__":
    print("\nTest begins...\n")

    # ~ADD TEST CASE HERE~
    # test case arg format: (arg1, arg2, ..., correct_out)
    test_cases = [
        ["geek", "eke", 5],
        ["AGGTAB", "GXTXAYB", 9]
    ]

    correct = 0
    current = 0
    for t in test_cases:
        print("Test {}:".format(current))
        t1 = time.time()
        ans = solution(t[0], t[1])
        duration = time.time() - t1
        if ans != t[2]:
            def error(got, correct):
                print("\tERROR: Got {}. Should be {}".format(got, correct))
            error(ans, t[2])
        else:
            correct += 1
            print("\tPASSED")
        current += 1
    print("\n{} of {} correct\n".format(correct, len(test_cases)))