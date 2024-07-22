class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = zip(names, heights)
        sortedDict = sorted(d, key=lambda item: item[1], reverse = True)
        return [s[0] for s in sortedDict]