class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # core logic: group the anagrams together yto grop these build a hashmap of their key and tehir words and return the values as a list 

        # build a hashmap 
        # key is the ord array 
        # value is the word 
        res = defaultdict(list) # value is list of values
        for s in strs:
            count = [0] * 26 
            for c in s:
                count[ord(c)-ord('a')] +=1
            res[tuple(count)].append(s)
        return list(res.values())



    
