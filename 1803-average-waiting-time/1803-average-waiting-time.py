class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        ava_at = 0
        total_wait =0
        for a , t in customers:
            ava_at = max(ava_at, a)+t
            total_wait += ava_at - a
        return total_wait / len(customers)