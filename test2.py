class Store:
    def __init__(self, name, address, items):
        self.name = name
        self.address = address
        self.items = {}


    def add_item(self, item_name, price):
        self.items[item_name] = price
        print((f"Товар {item_name} добавлен в магазин {self.name} по цене {price}"))

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар {item_name} удален из магазина {self.name}")



    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена {item_name} обновлена в магазине {self.name} на {new_price}")
        else:
            print(f"Товар {item_name} не найден в магазине {self.name}")

store_items = [
    {"name": "Apples", "price": 1.99},
    {"name": "Bananas", "price": 2.99},
    {"name": "Cherries", "price": 3.49}
]


shop1 = Store("shop1", "address1", store_items)


shop2 = Store("shop2", "address2", store_items)
shop3 = Store("shop3", "address3", store_items)

shop1.add_item("Apples", 1.99)
shop1.add_item("Bananas", 2.99)
shop1.add_item("Cherries", 3.49)


#shop1.remove_item("Apples")
print(shop1.get_price("Bananas"))
shop1.update_price("Cherries", 3.55)
print(shop1.items)