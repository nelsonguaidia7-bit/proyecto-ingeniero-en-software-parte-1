from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Usamos un conjunto para almacenar los números únicos
        seen = set()

        for num in nums:
            if num in seen:
                return True # Si encontramos un número que ya está en el conjunto, significa que hay un duplicado
            seen.add(num) # Agregamos el número al conjunto si no estaba presente 

        return False # Si terminamos el bucle sin encontrar duplicados, devolvemos False

# Prueba local para verificar
if __name__ == "__main__":
    sol = Solution()
    print("¿Tiene duplicados [1, 2, 3, 1]?:", sol.containsDuplicate([1, 2, 3, 1])) # Debe dar True
    print("¿Tiene duplicados [1, 2, 3, 4]?:", sol.containsDuplicate([1, 2, 3, 4])) # Debe dar False