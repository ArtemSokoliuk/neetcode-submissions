class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        lengths = []
        curr_len = 0
        for i in nums:
            if i == 1:
                curr_len += 1
            else:
                lengths.append(curr_len)
                curr_len = 0
        if curr_len:
            lengths.append(curr_len)
        return max(lengths)