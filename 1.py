import random
import time
import matplotlib.pyplot as plt

# тупо списки
sizes = []
times = []

# от 1тыс. до 100тыс. с шагом 1тыс.
for size in range(1000, 101000, 1000):
# стартуем
start = time.time()

# делаем список
r = [random.randint(1, 100) for _ in range(size)]

# конченое время
end = time.time()
c = end - start

# размер и время
sizes.append(size)
times.append(c)

# график
plt.figure(figsize=(10, 6))
plt.plot(sizes, times, marker='o', linestyle='-')
plt.title('Зависимость времени создания списка от его размера')
plt.xlabel('Размер списка')
plt.ylabel('Время создания (секунды)')
plt.grid(True)

# показываем
plt.show()
