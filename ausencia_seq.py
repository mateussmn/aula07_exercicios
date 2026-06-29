#Encontrar Valores Ausentes em uma Sequência

from typing import List

sequencia: List = [1,2,3,4,6,8,9,11]

def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return sorted(list(completo - set(sequencia)))

sequencia_formatada = ", ".join(str(num) for num in sequencia)

ausente = encontrar_valores_ausentes(sequencia)
ausentes_formatado = ", ".join(str(num) for num in ausente)

print(f"Os numeros que faltam na sequencia {sequencia_formatada} são: {ausentes_formatado}")