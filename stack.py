class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

    # Prueba local
if __name__ == "__main__":
    sol = Solution()
    print("¿Es válido '()[]{}'?:", sol.isValid("()[]{}")) # Debe dar True
    print("¿Es válido '(]'?:", sol.isValid("(]"))         # Debe dar False
 