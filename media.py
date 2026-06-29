#Calcular Média de Valores em uma Lista
from typing import List

valores = [4,6,8,9,22,42]

def calcular_media(valores: List[float]) -> float:
    media = sum(valores) / len(valores)
    return media

media: float = calcular_media(valores)
print(media)