import matplotlib.pyplot as plt

# Створюємо порожні списки для координат
x = []
y = []

# Зчитуємо дані з датасету
with open('DS4.txt', 'r') as file:
    for line in file:
        coords = line.split()
        if len(coords) == 2:
            x.append(int(coords[0])) 
            y.append(int(coords[1]))

# Встановлює розмір (960x540 пікселів) та будує графік
plt.figure(figsize=(9.6, 5.4), dpi=100)
plt.scatter(x, y, color='black', s=5)
plt.xlim(0, 960)
plt.ylim(0, 540)

# Збергіає результат в пнг
plt.savefig('result.png')
plt.close()

print("Графік успішно збережено у файл result.png")