#Day 3

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        return countS == countT

# Prueba local para verificar
if __name__ == "__main__":
    sol = Solution()
    print("¿Es anagrama (anagram / nagaram)?:", sol.isAnagram("anagram", "nagaram")) # Debe dar True
    print("¿Es anagrama (rat / car)?:", sol.isAnagram("rat", "car"))                 # Debe dar False
