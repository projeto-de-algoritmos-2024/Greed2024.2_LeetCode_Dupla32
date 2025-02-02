class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        soma = 0
        costs.sort(key=lambda x: x[0] - x[1])
        tamanho = len(costs) // 2

        for i in range(tamanho):
            soma += costs[i][0]
            soma += costs[tamanho + i][1]


        return soma