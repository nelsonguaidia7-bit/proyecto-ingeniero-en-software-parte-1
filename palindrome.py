class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Paso 1: Limpiar la cadena (convertir a minúsculas y quitar caracteres no alfanuméricos)
        # '.isalnum()' verifica si un caracter es letra o número
        cleaned_s = "".join(char.lower() for char in s if char.isalnum())
        
        # Paso 2: Aplicar los dos punteros en la cadena ya limpia
        left = 0
        right = len(cleaned_s) - 1
        
        while left < right:
            if cleaned_s[left] != cleaned_s[right]:
                return False
            left += 1
            right -= 1
            
        return True

# Prueba local para verificar
if __name__ == "__main__":
    sol = Solution()
    print("¿Es palíndromo (A man, a plan, a canal: Panama)?:", sol.isPalindrome("A man, a plan, a canal: Panama")) # True
    print("¿Es palíndromo (race a car)?:", sol.isPalindrome("race a car")) # False