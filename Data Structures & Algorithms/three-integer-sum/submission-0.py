class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left<right:
                cur_sum = nums[left]+nums[i]+nums[right]
                if cur_sum == 0:
                    res.add(tuple([nums[i],nums[left],nums[right]]))
                    left+=1
                    right-=1
                elif cur_sum < 0:
                    left+=1
                else:
                    right-=1
                    
        
        return [list(i) for i in res]