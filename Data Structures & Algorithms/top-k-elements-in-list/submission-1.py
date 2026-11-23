class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        int_freq = defaultdict(int)
        for i in nums:
            int_freq[i]+=1
        return sorted(int_freq, key=int_freq.get, reverse=True)[:k]