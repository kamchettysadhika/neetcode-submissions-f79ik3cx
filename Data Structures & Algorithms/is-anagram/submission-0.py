class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Map1= {}
        for string  in s:
            Map1[string] = Map1.get(string, 0) + 1 
        Map2 = {}
        for string2 in t:
            Map2[string2] = Map2.get(string2, 0) + 1 
        return Map1 == Map2