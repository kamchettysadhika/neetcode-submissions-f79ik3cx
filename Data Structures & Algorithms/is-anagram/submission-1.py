class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if teh hashmap is equal 
        # need 2 maps 
        mapS = {}
        mapT = {}
        # initial check [len(s) == len(teh)]
        if len(s) == len(t):
            for ch in s:
                mapS[ch]= 1+ mapS.get(ch,0)
            for ch in t:
                mapT[ch]= 1+ mapT.get(ch,0)

            return mapS == mapT 


        # build a hashmap of s 
        return False 
