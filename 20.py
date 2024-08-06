class Product:
    def __init__(self, code, name, price):
        self.name = name
        self.code = code
        self.price = price
        self.count = 1


class Basket:
    def __init__(self, id):
        self.id = id
        self.items = []
        self.total_price = 0
        self.count = len(self.items)
        self.total = 0
        self.discount = False

    def apply_discount(self, code):
        codes = {"10010": 10, "10020": 20, "10030": 30}

        if not self.discount:
            if code in codes:
                self.total -= self.total * (codes[code] / 100)
                self.discount = True
                print(f"Applied {codes[code]}% discount")
        else:
            print("You can't use the discount more than once")

    def add_item(self, prd):
        if prd in self.items:
            pass
        else:
            self.items.append(prd)
            print(f"{prd.name} added to basket")
            print('-' * 50)

    def remove_item(self, prd):
        if prd in self.items:
            self.items.remove(prd)
            print(f"{prd.name} removed from basket")
            print('-' * 50)
        else:
            print(f"{prd.name} is not in your basket")

    def factor(self):
        prices = []
        for i in self.items:
            prices.append(i.price)

        self.total = sum(prices)
        print("Total :", sum(prices))


product1 = Product("dkp-15500620", "Zenbook Pro Duo 14", 94.999)
product2 = Product("dkp-9674062", "Spectre x360", 92.990)
product3 = Product("dkp-16002846", "Predator Helios Neo 16", 104.999)

amir_basket = Basket(1001)

amir_basket.add_item(product1)
amir_basket.add_item(product2)
amir_basket.add_item(product3)

amir_basket.remove_item(product1)

amir_basket.apply_discount("10010")

amir_basket.factor()

# Must be fixed : takhfif rooye jam sabad tasir nemizare
