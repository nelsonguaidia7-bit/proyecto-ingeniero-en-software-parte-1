from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # 1. Calculamos el ancho entre los dos punteros
            width = right - left
            
            # 2. La altura estará limitada por la pared más baja
            current_height = min(height[left], height[right])
            
            # 3. Calculamos el agua actual y actualizamos nuestro récord
            current_water = width * current_height
            max_water = max(max_water, current_water)
            
            # 4. Movemos el puntero de la pared más baja en busca de una más alta
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water

# Prueba local
if __name__ == "__main__":
    sol = Solution()
    print("Máxima agua almacenada [1,8,6,2,5,4,8,3,7]:", sol.maxArea([1,8,6,2,5,4,8,3,7])) # Debe dar 49