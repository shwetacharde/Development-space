# ps - https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_num = dict()
        for i in range(len(nums)):
            req = target - nums[i]
            if req in map_num:
                return [map_num[req], i]
            map_num[nums[i]] = i
