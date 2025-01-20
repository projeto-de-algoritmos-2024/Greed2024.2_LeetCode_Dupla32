class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        lista = []
        for i in range(n):
            lista.append([ speed[i], efficiency[i]])
        
        lista.sort(key = lambda x: x[0] * x[1], reverse = True)

        velocidade_total = 0
        eficiencia_total = float("inf")

        for j in range(k):
            velocidade_total += lista[j][0]
            eficiencia_total = min(eficiencia_total, lista[j][1])
        
        return velocidade_total * eficiencia_total