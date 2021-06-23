print("12")
lists = [1, 2, 3, 4, 5, 6]
for list in lists:
    print(list)

# Объединить два множества
cars = {"BMW", "Toyota", "Honda"}
new_cars = {"Tesla", "Smart"}
all_cars = cars.union(new_cars)
print(all_cars)

# Проверка на пересечение
cars = {"BMW", "Toyota", "Honda"}
new_cars = {"Toyota", "Tesla", "Smart"}
intersection = cars.intersection(new_cars)
print(intersection)

# Получить список элементов, не входящих во второе множество
cars = {"BMW", "Toyota", "Honda"}
new_cars = {"Toyota", "Tesla", "Smart"}
difference = cars.difference(new_cars)
print(difference)

def car():
 # Счётчик количества поездок
    trip = 0
    def start():
         nonlocal trip
         trip += 1
         car_name = "Tesla Model X"
         print(car_name + " начала движение!")
         print("Номер поездки: " + str(trip))
    return start
car = car()
car()
car()
car()
car()

# Добавить новый элемент по индексу
# first = list([1, 2, 3, 4, 5, 6])
# first.insert(0, 100)
# print(first)

# # Получение индекса по значению элемента
# first = list([1, 2, 3, 4, 5, 6, "Марк"])
# print(first.index("Марк"))


count = 15
while count != 0:
    count -= 1
    print("Итерация номер: " + str(count))


