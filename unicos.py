#Contar Valores Únicos em uma Lista
from typing import List

lista: List = [10, 20, 20, 30, 10, 40]

def contar_valores_unicos(lista: List[int]) -> int:
    return len(set(lista))

print(contar_valores_unicos(lista))