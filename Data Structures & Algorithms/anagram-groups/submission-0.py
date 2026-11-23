class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = defaultdict(list)
        for s in strs:
            a = ''.join(sorted(s))
            group_dict[a].append(s)
        return list(group_dict.values())

         