class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        total = sum(nums)
        ans = 1000000000
        mid = (len(nums)) // 2
        nums1 = nums[:mid]
        nums2 = nums[mid:]
        dict1 = {}
        dict2 = {}
        
        for i in range((1 << mid)):
            s1 = 0
            s2 = 0
            for j in range(mid):
                if i & (1 << j):
                    s1 += nums1[j]
                    s2 += nums2[j]
            key = i.bit_count()
            if key not in dict1:
                dict1[key] = []
            if key not in dict2:
                dict2[key] = []
            dict1[key].append(s1)
            dict2[key].append(s2)
        
        half = total // 2
        
        for key in dict1.keys():
            list1 = dict1[key]
            list2 = sorted(dict2[mid - key])

            for item1 in list1:
                item2  = half - item1
                idx = bisect_left(list2, item2)

                for i in [idx, idx-1]:
                    if 0 <= i < len(list2):
                        ans = min(ans, abs(total - 2 * (item1 + list2[i])))
        
        return ans