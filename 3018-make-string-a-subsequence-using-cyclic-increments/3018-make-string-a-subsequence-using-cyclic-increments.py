class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        count = 0
        for i in range(len(str1)):
            if count == len(str2):
                return True
            if str1[i] == 'z' and str2[count] == 'a':
                count+=1
            elif ord(str2[count]) - ord(str1[i]) == 1 or ord(str1[i]) - ord(str2[count]) == 0:
                count += 1
        if count == len(str2):
            return True
            
        return False