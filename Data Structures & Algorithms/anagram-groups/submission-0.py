class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
     res = defaultdict(list)
     for str in strs:
        arr = [0] * 26 
        for c in str:
            numAlphabet = ord(c) - ord('a')
            arr[numAlphabet] +=1 

        res[tuple(arr)].append(str)
     return list(res.values())
# We are building a map of teh count fof teh alphabets where key is teh 
# tuple of teh alphabet count and value is the word itself 
# so we basically have a grouping of anagrams as values so we can retrn those values 




    
