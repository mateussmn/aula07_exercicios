#Calcular Média de Valores em uma Lista
from typing import List

def calcular_media(valores: List[float]) -> float:
    return sum(valores) / len(valores)