class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = [0] * n
        
        # Compute in-degrees
        for u, v in edges:
            in_degree[v] += 1
        
        #Find nodes with in-degree 0
        champions = [i for i in range(n) if in_degree[i] == 0]
        
        # Determine the result
        if len(champions) == 1:
            return champions[0]  # Unique champion found
        else:
            return -1  # No unique champion