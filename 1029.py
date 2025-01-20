class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        soma = 0
        costs.sort(key=lambda x: x[0] )
        tamanho = len(costs)/ 2
        tamanho_a = 0

        for n in costs:
            if n[0] <= n[1] or tamanho_a < tamanho:
                tamanho_a += 1
                soma += n[0]
            else:
                soma += n[1]

        return soma