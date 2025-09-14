class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words_perfect = set(wordlist)
        words_cap = {}
        words_vow = {}

        for word in wordlist:
            wordlow = word.lower()
            words_cap.setdefault(wordlow, word)
            words_vow.setdefault(self._devowel(wordlow), word)
        
        return [self._solve(querie, words_perfect, words_cap, words_vow) for querie in queries]

    def _devowel(self, word: str) -> str:
        return "".join("*" if w in "aeiou" else w for w in word)

    def _solve(self, query: str, words_perfect: set, words_cap: dict, words_vow: dict) -> str:
        if query in words_perfect:
            return query
        
        queryL = query.lower()
        if queryL in words_cap:
            return words_cap[queryL]

        queryD = self._devowel(queryL)
        if queryD in words_vow:
            return words_vow[queryD]

        return ""