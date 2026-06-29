#Converter Celsius para Fahrenheit em uma Lista
from typing import List

temperaturas_celsius: List = [22, 33, 40, 16, 6]

def celsius_para_fahrenheit(temperaturas_celsius: List[float]) -> List[float]:
    return [(9/5) * temp + 32 for temp in temperaturas_celsius]

for celsius, fahrenheit in zip(temperaturas_celsius, celsius_para_fahrenheit(temperaturas_celsius)):
    print(f"A temperatura em celsius é {celsius} e, em fahrenheit é {fahrenheit}")