class Product:
    """
    Класс Product представляет собой модель продукта с атрибутами name, weight и category.
    """
    def __init__(self, name, weight, category):
        # Инициализация объекта Product
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        # Возвращает строковое представление объекта Product
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    """
    Класс Shop представляет собой модель магазина, который управляет списком продуктов в файле.
    """
    def __init__(self):
        # Инициализация объекта Shop с инкапсулированным атрибутом __file_name
        self.__file_name = 'products.txt'

    def get_products(self):
        # Открываем файл и считываем его содержимое
        try:
            file = open(self.__file_name, 'r')
            content = file.read()
            file.close()  # Закрываем файл
            return content
        except FileNotFoundError:
            return ""

    def add(self, *products):
        # Добавляет продукты в файл __file_name, если их ещё нет в файле
        existing_products = self.get_products().splitlines()
        with open(self.__file_name, 'a') as file:
            for product in products:
                product_str = str(product)
                if product_str not in existing_products:
                    file.write(f'{product_str}\n')
                    print(product_str)
                else:
                    print(f'Продукт {product.name},{product.weight},{product.category} уже есть в магазине')


# Пример создания объектов классов Product и Shop, и вызова метода add
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__
s1.add(p1, p2, p3)
print("\nТекущие продукты в магазине:")
print(s1.get_products())
