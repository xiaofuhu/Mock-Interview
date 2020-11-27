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
import time

dp = None

def lcs_length_dp(str1, str2):
    len1, len2 = len(str1), len(str2)
    if len1 == 0 or len2 == 0:
        return 0
    if (dp[len1 - 1][len2 - 1] != -1):
        return dp[len1 - 1][len2 - 1]
    elif str1[0] == str2[0]:
        dp[len1 - 1][len2 - 1] = 1 + lcs_length_dp(str1[1:], str2[1:])
        return dp[len1 - 1][len2 - 1]
    else:
        dp[len1 - 1][len2 - 1] = max(lcs_length_dp(str1[1:], str2), lcs_length_dp(str1, str2[1:]))
        return dp[len1 - 1][len2 - 1]

def lcs_length(str1, str2):
    len1, len2 = len(str1), len(str2)
    if len1 == 0 or len2 == 0:
        return 0
    if str1[0] == str2[0]:
        return 1 + lcs_length(str1[1:], str2[1:])
    return max(lcs_length(str1[1:], str2), lcs_length(str1, str2[1:]))

def solution2(str1, str2):
    # Set up dp buffer
    len1, len2 = len(str1), len(str2)
    global dp
    dp = [[-1 for j in range(len2)] for i in range(len1)]
    # Find longest common subsequence
    len_of_lcs = lcs_length_dp(str1, str2)
    # Calculate length of shortest supersequence
    return len(str1) + len(str2) - len_of_lcs

def solution1(str1, str2):
    # Find longest common subsequence with dynamic programming
    len_of_lcs = lcs_length(str1, str2)
    # Calculate length of shortest supersequence
    return len(str1) + len(str2) - len_of_lcs

if __name__ == "__main__":
    print("\nTest begins...\n")
    
    # ~ADD TEST CASE HERE~
    # test case arg format: (arg1, arg2, ..., correct_out)
    test_cases = [
        ["geek", "eke", 5],
        ["AGGTAB", "GXTXAYB", 9],
        ["", "Xswl", 4],
        ["XXX", "xXxXx", 6],
        ["LoLoLoKoKoK", "LLooK", 11],
        ["outrageous cactus", "o c s BALABA", 25],
    ]

    correct = 0
    current = 0
    for t in test_cases:
        print("Test {}:".format(current))
        t1 = time.time()
        ans = solution2(t[0], t[1])
        duration = (time.time() - t1) * 1000
        if ans != t[2]:
            def error(got, correct):
                print("\tERROR: Got {}. Should be {}".format(got, correct))
            error(ans, t[2])
        else:
            correct += 1
            print("\tPASSED\tTook {:.4f} ms".format(duration))
        current += 1
    print("\n{} of {} correct\n".format(correct, len(test_cases)))

# TIME Complexity: O(MN)
# SPACE Complexity: O(MN)