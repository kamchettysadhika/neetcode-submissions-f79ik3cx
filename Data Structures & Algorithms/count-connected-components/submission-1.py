class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # number of dfs you can perform -> number of connected components 
        # build teh graph 
        adjList = [[] for i in range(n)]
        visit  = [False] * n 
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        # define dfs 
        def dfs(node):
            for nei in adjList[node]:
                if not visit[nei]:
                    visit[nei]= True 
                    dfs(nei)
                

        # then  apply dfs on node
        res = 0 
        for node in range(n):
            if not visit[node]:
                visit[node] = True 
                dfs(node)
                res+=1 
        return res