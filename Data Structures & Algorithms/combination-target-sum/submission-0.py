class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i, cur, total):
            # basecases: possible 
            if total == target:
                result.append(cur.copy())
                return 
            # basecases :impossible 
            if i >= len(nums) or total > target:
                return 
            cur.append(nums[i])
            dfs(i,cur,total+nums[i])
        
            # dont include 
            cur.pop()
            dfs(i+1,cur,total)

        dfs(0,[],0)
        return result

