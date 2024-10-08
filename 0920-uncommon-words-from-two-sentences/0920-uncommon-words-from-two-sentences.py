class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        arr1 = [word for word in s1 if s1.count(word) == 1 and word not in s2]
        arr2 = [secWord for secWord in s2 if s2.count(secWord) == 1 and secWord not in s1]
        return arr1+arr2