"""
Esctructura de datos

"""

list = [100, "Laptop", "Microfono", 300.10]
data = {"name": "Roberto", "elements": list}
tpl = ('CANCELLED', 'COMPLETED', 'PENDING')

print(len(list))
list.append(5.5)
print(len(list))

for item in data.items():
    print(item)

c = data['name'][1]
print(c)
d = data.get("amount")
if d is None:
    print("No encontro")
else:
    print("encontrado")
