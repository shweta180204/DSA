'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start,end=0,len(s)-1
        while start<end:
            if not s[start].isalnum():
                start+=1
                continue
            if not s[end].isalnum():
                end-=1
                continue
            elif s[start].lower()!=s[end].lower():
                return False
            else:
                start+=1
                end-=1
        return True  

            
        
