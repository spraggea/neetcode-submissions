class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): #Edgecase
            return False
        
        countsT = {}
        countsS = {}

        for char in s:
            if char in countsT:
                countsT[char] += 1
            else:
                countsT[char] = 1
        
        for char in t:
            if char in countsS:
                countsS[char] += 1
            else:
                countsS[char] = 1

        return countsT == countsS

        