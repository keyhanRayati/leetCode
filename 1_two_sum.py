from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i,num in enumerate(nums):
            if target - num in dict:
                return [dict[target - num] , i]
            else:
                dict[num] = i
            

class __main__():
    instance = Solution()
    print(instance.twoSum([3,2,4] , 6 ))
