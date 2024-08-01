'''
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def sets(i,l):
            if i==len(nums):
                res.append(l[:])
                return
            l.append(nums[i])
            sets(i+1,l)
            l.pop()
            sets(i+1,l)


        res=[]
        sets(0,[])
        return res


        
