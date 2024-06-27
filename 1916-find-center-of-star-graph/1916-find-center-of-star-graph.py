class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)+1
        degree = [0]*(n+1)

        for u,v in edges:
            degree[u]+=1
            degree[v]+=1
            if degree[u]==n-1:
                ans = u
            elif degree[v]==n-1:
                ans = v

        return ans