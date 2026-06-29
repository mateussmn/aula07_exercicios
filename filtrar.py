#Filtrar Dados Acima de um Limite
valores = [4,6,8,9,22,42]

def filtrar_acima_de(valores: List[float], limite: float) -> List[float]:
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado

limite = float(input("Digite um valor limite: "))

resultado = filtrar_acima_de(valores, limite)
print(resultado)

