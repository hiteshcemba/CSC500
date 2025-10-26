motorcycles = {"Ducati": "Monster", "Harley": "Sportster", "Triumph": "Bonneville", "Aprilia": "RSV4"}
print(motorcycles)
del motorcycles["Triumph"]
print(motorcycles)

# Inconsistent Output
# {'Ducati': 'Monster', 'Harley': 'Sportster', 'Triumph': 'Bonneville', 'Aprilia': 'RSV4'}
# {'Ducati': 'Monster', 'Harley': 'Sportster', 'Aprillia': 'RSV4'}
