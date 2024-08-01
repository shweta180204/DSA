'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


'''



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m=0
        l=0
        w=set()
        for r in range(len(s)):
            while s[r] in w:
                w.remove(s[l])
                l+=1
            w.add(s[r])
            m=max(m,r-l+1)
        return m


        
