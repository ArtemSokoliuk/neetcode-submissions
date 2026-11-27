class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [1]*length*2

        for idx, val in enumerate(nums):
            ans[idx] = ans[idx+length] = val

        return ans
