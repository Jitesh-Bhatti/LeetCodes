def convert(s, numRows):
    rows = [""] * numRows
    direction = -1 
    current_row = 0
    for i in s:
        rows[current_row] += i
        if current_row == 0 or current_row == numRows - 1:
            direction *= -1
    return "".join(rows)


convert("abcdefg", 3)