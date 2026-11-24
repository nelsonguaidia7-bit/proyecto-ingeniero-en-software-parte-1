from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0      # Día de compra (precio más bajo encontrado)
        max_profit = 0 # Récord de ganancia máxima
        
        # El puntero right recorre cada día vendiendo
        for right in range(len(prices)):
            # Si encontramos un precio menor al de compra, actualizamos el punto de compra
            if prices[right] < prices[left]:
                left = right
            else:
                # Si no, calculamos la ganancia actual y actualizamos el récord
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)
                
        return max_profit

# Prueba local
if __name__ == "__main__":
    sol = Solution()
    print("Ganancia máxima [7,1,5,3,6,4]:", sol.maxProfit([7, 1, 5, 3, 6, 4])) # Debe dar 5
    print("Ganancia máxima [7,6,4,3,1]:", sol.maxProfit([7, 6, 4, 3, 1]))       # Debe dar 0


    