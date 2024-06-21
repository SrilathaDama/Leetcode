class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix) #no.of rows
        m = len(matrix[0]) #no.of columns

        ans = []
        top = 0
        left = 0
        right = m-1
        bottom = n-1

        while top <= bottom and left<=right:

            for i in range(left, right+1):
                ans.append(matrix[top][i])
            top+=1

            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right-=1

             # For moving right to left.
            if (top <= bottom):
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])

                bottom -= 1

        # For moving bottom to top.
            if (left <= right):
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])

                left += 1

        return ans
            