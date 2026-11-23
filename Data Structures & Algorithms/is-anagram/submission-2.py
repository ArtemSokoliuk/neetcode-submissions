class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_word = defaultdict(int)
        t_word = defaultdict(int)
        for i in s:
            s_word[i]+=1
        for i in t:
            t_word[i]+=1
        return s_word==t_word        
