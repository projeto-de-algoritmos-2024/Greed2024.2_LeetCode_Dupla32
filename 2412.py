class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        # tem que ordenar de um jeito que atenda em qualquer ordem de transação logo a pior 
        # é deixar a que tem menos cashback primeiro e as que tem mais por ultimo

        transactions.sort(key = lambda x: x[1])
        valor_necessario = 0
        tamanho = len(transactions)

        for transacao in transactions:
            valor_necessario += transacao[0] - transacao[1]
        valor_necessario += ( transactions[tamanho - 1][1]) # o ultimo cashback n entra na soma
        return valor_necessario
