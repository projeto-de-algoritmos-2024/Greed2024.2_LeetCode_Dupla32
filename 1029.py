class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        soma = 0
        for n in costs:
            if n[0] <= n[1]:
                soma += n[0]
            else:
                soma += n[1]
        return soma