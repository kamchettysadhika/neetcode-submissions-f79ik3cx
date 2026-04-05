class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0 
        count_w = 0 
        res = len(blocks)
        for r in range(len(blocks)):
          if blocks[r] == "W":
            count_w+=1 
          if (r-l+1) == k:
            res = min(count_w,res)
            if blocks[l] == "W":
              count_w -=1 
            l+=1
            
        return res
              