# СПИСОК ОБЪЕКТОВ

from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy_S24_Ultra", "+79215557744"),
    Smartphone("Apple", "iPhone_16_Pro", "+79113334455"),
    Smartphone("Huawei", "Pura_70_Ultra", "+79604442266"),
    Smartphone("Xiaomi", "Mi_14T_Pro",  "+79537774433"),
    Smartphone("OnePlus", "12", "+79881114477")
]

for phone in catalog:
    print(f'{phone.brand} - {phone.model}. {phone.number}')
