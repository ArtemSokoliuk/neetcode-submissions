class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            diff_num = target - num
            if diff_num in nums_dict:
                return [nums_dict[diff_num], i]
            nums_dict[num] = i