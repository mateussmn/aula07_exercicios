#Calcular Desvio Padrão de uma Lista

from typing import List

valores: List = [22, 33, 40, 16, 6, 8, 12]

def calcular_desvio_padrao(valores: List[float]) -> float:
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return variancia ** 0.5

print(round(calcular_desvio_padrao(valores),2))