class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for i in s:
            if i.isalnum():
                newstr = newstr + i.lower()
        return newstr == newstr[::-1] # python code to reverse a string.