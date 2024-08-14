class Solution:
    def generateAnagramKey(self, word):
        """given a word, we generate a key that would be unique for different anagrams
        but will be the same for words that form same anagram """
        count = [0] * 26
        for c in word:
            count[ord(c) - ord('a')] += 1

        result = []
        for i in range(26):
            if count[i] != 0:
                result.extend([chr(i + ord('a')), str(count[i])])

        return ''.join(result)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we want to split the elements into sub-arrays based on some key 
        #once we generate the key, we need a map to store the key to a list of strings 
        anagramMap = defaultdict(list)
        res = []

        for word in strs:
            key = self.generateAnagramKey(word)
            anagramMap[key].append(word)
        
        for anagram in anagramMap.keys():
            res.append(anagramMap[anagram])
        
        return res
