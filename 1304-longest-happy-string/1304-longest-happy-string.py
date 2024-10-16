import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0: heapq.heappush(pq, (-a, 'a'))
        if b > 0: heapq.heappush(pq, (-b, 'b'))
        if c > 0: heapq.heappush(pq, (-c, 'c'))

        res = []
        while pq:
            cnt1, char1 = heapq.heappop(pq)
            if len(res) >= 2 and res[-1] == char1 and res[-2] == char1:
                if not pq:
                    break
                cnt2, char2 = heapq.heappop(pq)
                res.append(char2)
                cnt2 += 1
                if cnt2:
                    heapq.heappush(pq, (cnt2, char2))
            else:
                res.append(char1)
                cnt1 += 1
            if cnt1:
                heapq.heappush(pq, (cnt1, char1))
        
        return ''.join(res)