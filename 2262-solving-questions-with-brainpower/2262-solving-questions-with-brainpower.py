class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:

        n = len(questions)
        ans = [0] * (n - 1) + [questions[-1][0]]
        
        for i in range(n-2, -1,-1):
            pts, bp = questions[i]
            if bp+i+1 < n: ans[i]= max(ans[i+1], pts+ans[bp+i+1])
            else         : ans[i]= max(ans[i+1], pts)
                
        return ans[0]