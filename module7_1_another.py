class Product:
    """
    Класс Product представляет собой модель продукта с атрибутами name, weight и category.
    """
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    """
    Класс Shop представляет собой модель магазина, который управляет списком продуктов в файле.
    """
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ""

    def add(self, *products):
        existing_products = self.get_products().splitlines()
        with open(self.__file_name, 'a') as file:
            for product in products:
                product_str = str(product)
                if product_str not in existing_products:
                    file.write(f'{product_str}\n')
                    print(product_str)
                else:
                    print(f'Продукт {product.name} уже есть в магазине')


# Пример создания объектов классов Product и Shop, и вызова метода add
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

# Первый запуск
print("Первый запуск:")
s1.add(p1, p2, p3)

# Второй запуск
print("\nВторой запуск:")
s1.add(p1, p2, p3)

# Вывод содержимого файла после добавления продуктов
print("\nТекущие продукты в магазине:")
print(s1.get_products())