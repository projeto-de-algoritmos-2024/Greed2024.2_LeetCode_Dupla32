from typing import List

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        sementes = list(zip(plantTime, growTime))
        sementes.sort(key=lambda x: -x[1])  # Ordenar por maior growTime
        
        tempo_plantio_atual = 0
        dia_maximo_florescimento = 0
        
        for tempo_plantio, tempo_crescimento in sementes:
            tempo_plantio_atual += tempo_plantio
            dia_maximo_florescimento = max(dia_maximo_florescimento, tempo_plantio_atual + tempo_crescimento)
        
        return dia_maximo_florescimento
