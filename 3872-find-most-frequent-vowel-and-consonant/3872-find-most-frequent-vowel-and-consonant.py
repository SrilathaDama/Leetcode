class Solution:
    def maxFreqSum(self, s: str) -> int:
        maxFreqVowel, maxFreqCons = 0, 0

        letterToCount = collections.Counter(s)
        for letter in letterToCount:
            count = letterToCount[letter]
            if letter in "aeiou":
                maxFreqVowel = max(maxFreqVowel, count)
            else:
                maxFreqCons = max(maxFreqCons, count)
        
        return maxFreqVowel + maxFreqCons