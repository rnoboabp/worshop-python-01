"""
Taller01: Bases en python.
- Variables
- Operadores
- Estructura de datos
"""

# Iniciando desarrollo con python
# mypy
customer_name: str = "Roberto"  # PEP8
print(customer_name)
DNI_BASIC = "999999"
customer_name = 100
print(customer_name)

######

if customer_name > 20:
    print("Hello World python!")
elif customer_name < 10:
    print("caso contrario")
else:
    print("///")

# range [0,19]
for item in range(20):
    print(item)