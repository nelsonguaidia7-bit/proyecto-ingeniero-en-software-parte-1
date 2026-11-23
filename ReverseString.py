class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left] 
            left += 1
            right -= 1

# Prueba local
if __name__ == "__main__":
    sol = Solution()
    test_string = ["h", "e", "l", "l", "o"]
    sol.reverseString(test_string)
    print("Cadena invertida:", test_string)  # Debe dar ['o', 'l', 'l', 'e', 'h']