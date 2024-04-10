class Solution:
    def isPalindrome(self,x:int) ->bool:
        str_x = str(x)
        print(str_x == str_x[::-1])
