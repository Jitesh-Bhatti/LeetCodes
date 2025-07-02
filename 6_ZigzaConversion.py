''' 

6. Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
'''

class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        rows = [""] * numRows
        direction = -1 
        current_row = 0
        for i in s:
            rows[current_row] += i
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1
            current_row += direction
        return "".join(rows)

A = Solution()

print(A.convert("abcdefg", 3))