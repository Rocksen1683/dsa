class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we want to split the elements into sub-arrays based on some key 
        #once we generate the key, we need a map to store the key to a list of strings 
        anagramMap = defaultdict(list)
        res = []

        for word in strs:
            sortedWord = ''.join(sorted(word)) #sorting a string python
            anagramMap[sortedWord].append(word)
        
        for anagram in anagramMap.keys():
            res.append(anagramMap[anagram])
        
        return res
