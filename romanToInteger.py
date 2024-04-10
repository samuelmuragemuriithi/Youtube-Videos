# class Solution:
#     def romanToInt(self, s: str) -> int:
s = "MCMXCIV"
print(s)
roman_dict = {'I': 1, 'V': 5, 'X': 10,
                'L': 50, 'C': 100, 'D': 500, 'M': 1000}

result = 0
prev_value = 0

for char in s:
    current_value = roman_dict[char]
    print(current_value)
    if current_value > prev_value:
        result += current_value - 2 * prev_value
        print(f"result1: {result}, current_value: {current_value}, prev_value: {prev_value}", end='\n\n')
    else:
        result += current_value
        print(f"result2: {result}, current_value: {current_value}, prev_value: {prev_value}", end='\n\n')

    prev_value = current_value
    print(f"prev_value: {prev_value}", end='\n\n')

print(result)
