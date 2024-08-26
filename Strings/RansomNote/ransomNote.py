class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #use a counter to check if ransomNote can be constructed
        magazineCount = Counter(magazine)

        for ch in ransomNote:
            if ch not in magazineCount or magazineCount[ch] == 0:
                return False

            magazineCount[ch] -= 1 

        return True