from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0  # Día de compra (puntero izquierdo)
        right = 1 # Día de venta (puntero derecho)
        max_profit = 0
        
        while right < len(prices):
            # ¿Es rentable vender hoy respecto al día en que compramos?
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                # Si encontramos un precio aún más barato, movemos nuestra compra a ese día
                left = right
            
            # Avanzamos la ventana al siguiente día
            right += 1
            
        return max_profit

# Prueba local
if __name__ == "__main__":
    sol = Solution()
    print("Ganancia máxima [7, 1, 5, 3, 6, 4]:", sol.maxProfit([7, 1, 5, 3, 6, 4])) # Debe dar 5
    print("Ganancia máxima [7, 6, 4, 3, 1]:", sol.maxProfit([7, 6, 4, 3, 1]))       # Debe dar 0