class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = [0] * 1001
        result = []
        for i in nums1:
            arr[i]+=1
        for i in nums2:
            if arr[i]>0:
                result.append(i)
                arr[i] -= 1
        return result