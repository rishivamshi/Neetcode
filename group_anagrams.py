class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            x = ''.join(sorted(word))
            if x in d:
                d[x] = d[x] + [word]
            else:
                d[x] = [word]
        
        return list(d.values())
        
