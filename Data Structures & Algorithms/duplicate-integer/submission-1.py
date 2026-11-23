class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_exist = dict()
        for i in nums:
            if i in nums_exist:
                return True
            nums_exist[i] = 1
        return False

        