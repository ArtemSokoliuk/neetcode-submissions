class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        ans = [0]*2*nums_len
        for idx, num in enumerate(nums):
            ans[idx] = ans[idx+nums_len] = num
            idx+=1
        return ans