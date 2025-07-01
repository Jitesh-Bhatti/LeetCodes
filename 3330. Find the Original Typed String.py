'''

3330. Find the Original Typed String I

Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.

You are given a string word, which represents the final output displayed on Alice's screen.

Return the total number of possible original strings that Alice might have intended to type.

 

Example 1:

Input: word = "abbcccc"

Output: 5

Explanation:

The possible strings are: "abbcccc", "abbccc", "abbcc", "abbc", and "abcccc".
'''

class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        rep = {}
        letter = set()
        possibility = 0
        for i in word:
            if i not in rep:
                rep[i] = word.count(i)
                possibility += 1
        print(rep.values())
        a = 0
        for i in rep.values():
            if(i == 1):
                a = a+i
            else:
                a = a+i
                a -= 1
        if(a == possibility){
            return 1
        }
        else {
            return a
        }

A = Solution()
A.possibleStringCount("abcd")


# class Solution:
#     def possibleStringCount(self, word):
#         count = 0
#         for i in range(1, len(word)):
#             if word[i] == word[i - 1]:
#                 count += 1
#         return count + 1
