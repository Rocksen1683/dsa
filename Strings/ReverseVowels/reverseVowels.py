class Solution:
    def reverseVowels(self, s: str) -> str:
        #two pointer to reverse
        vowels = {'a', 'e', 'i', 'o',  'u'}
        #strings aren't mutable
        sList = list(s)
        l = 0 
        r = len(s) - 1

        while l < r:
            print(l, r)
            if sList[l].lower() in vowels and sList[r].lower() in vowels:
                temp = sList[l]
                sList[l] = sList[r]
                sList[r] = temp
                l += 1
                r -= 1
            if sList[l].lower() not in vowels:
                l += 1
            if sList[r].lower() not in vowels: 
                r -= 1

        return ''.join(sList)