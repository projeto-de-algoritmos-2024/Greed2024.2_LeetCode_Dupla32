class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        lista = []
        for i in range(n):
            lista.append([speed[i], efficiency[i]])
        
        lista.sort(key = lambda x: x[1], reverse = True)

        heap = []
        velocidade_total = 0
        resultado = 0

        for velocidade, eficiencia in lista:
            if len(heap) == k:
                velocidade_total -= heapq.heappop(heap)  
            
            heapq.heappush(heap, velocidade)
            velocidade_total += velocidade
            resultado = max(resultado, velocidade_total * eficiencia)

        return resultado % (10**9 + 7)