class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        treesum = []
        def sumtree(node, path):
            s = values[node]
            path.add(node)
            for child in graph[node]:
                if child not in path:
                    s += sumtree(child, path)
            treesum.append(s)
            path.remove(node)
            return s

        sumtree(0, set())
        return sum(1 for x in treesum if x%k==0)