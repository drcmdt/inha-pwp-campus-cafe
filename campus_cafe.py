"""Campus Cafe Practice — Reference Solution"""


daily_customer_counts = [18, 25, 21, 30]
daily_customer_counts.append(27)
daily_customer_counts.sort()


def analyze_customers(customer_counts):
    total_customers = sum(customer_counts)
    average_customers = total_customers / len(customer_counts)
    complete_groups = total_customers // 4
    customers_left = total_customers % 4

    print("Customer counts:", customer_counts)
    print("Total customers:", total_customers)
    print("Average customers:", average_customers)
    print("Complete groups of four:", complete_groups)
    print("Customers left over:", customers_left)


stock = {
    "Sandwich": 6,
    "Tea": 8,
    "Cake": 4
}

stock.update({"Juice": 5})
print("Tea in stock:", stock.get("Tea"))

practice_products = ["Tea", "Cake", "Juice"]
practice_products.remove("Cake")

practice_stock = stock.copy()
removed_cake = practice_stock.pop("Cake")
print("Removed Cake quantity:", removed_cake)


def show_stock(stock_data):
    print("\nCurrent stock:")
    for product, quantity in stock_data.items():
        print(product, "-", quantity)


class MenuItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        print(f"{self.name} costs {self.price} euros.")

    def calculate_price(self, quantity):
        return self.price * quantity

    def is_available(self, stock_data):
        return self.name in stock_data and stock_data.get(self.name, 0) > 0


class Drink(MenuItem):

    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def describe(self):
        super().describe()
        print(f"Size: {self.size}.")


class Order:

    def __init__(self):
        self.items = []

    def add_item(self, menu_item, quantity):
        order_line = {
            "item": menu_item,
            "quantity": quantity
        }
        self.items.append(order_line)

    def total_price(self):
        total = 0
        for order_line in self.items:
            item = order_line["item"]
            quantity = order_line["quantity"]
            total = total + item.calculate_price(quantity)
        return total

    def total_quantity(self):
        quantity = 0
        for order_line in self.items:
            quantity = quantity + order_line["quantity"]
        return quantity

    def show_order(self):
        print("\nOrder summary:")

        if len(self.items) == 0:
            print("The order is empty.")
        else:
            for order_line in self.items:
                item = order_line["item"]
                quantity = order_line["quantity"]
                line_price = item.calculate_price(quantity)
                print(item.name, "x", quantity, "=", line_price, "euros")


class Cafe:

    def __init__(self, name, menu, stock_data):
        self.name = name
        self.menu = menu
        self.stock = stock_data
        self.order = Order()

    def show_menu(self):
        print(f"\n{self.name} menu:")
        for index in range(len(self.menu)):
            print(index + 1, end=". ")
            self.menu[index].describe()

    def find_item(self, item_name):
        for item in self.menu:
            if item.name == item_name:
                return item
        return None

    def place_order(self, item_name, quantity):
        item = self.find_item(item_name)

        if item is None:
            print("Item not found.")
        elif quantity <= 0:
            print("Quantity must be positive.")
        elif not item.is_available(self.stock) or self.stock[item.name] < quantity:
            print("Not enough stock.")
        else:
            self.order.add_item(item, quantity)
            self.stock[item.name] = self.stock[item.name] - quantity
            print("Item added.")

    def show_report(self):
        self.order.show_order()

        total = self.order.total_price()
        item_count = self.order.total_quantity()

        print("Total price:", total, "euros")
        print("Total item quantity:", item_count)

        if total >= 20:
            print("Large order")
        elif total >= 10:
            print("Medium order")
        else:
            print("Small order")

        if item_count > 0:
            average_price = total / item_count
            print("Average price per item:", average_price, "euros")


sandwich = MenuItem("Sandwich", 5)
cake = MenuItem("Cake", 3)
tea = Drink("Tea", 2, "Medium")
juice = Drink("Juice", 4, "Large")

menu = [sandwich, cake, tea, juice]
campus_cafe = Cafe("Campus Cafe", menu, stock)


def run_cafe():
    running = True

    while running:
        print("\nMAIN MENU")
        print("1. Show cafe menu")
        print("2. Place an order")
        print("3. Show order report")
        print("4. Show stock")
        print("5. Exit")

        choice = input("Choose 1-5: ")

        match choice:
            case "1":
                campus_cafe.show_menu()
            case "2":
                item_name = input("Enter the exact item name: ")
                quantity = int(input("Enter quantity: "))
                campus_cafe.place_order(item_name, quantity)
            case "3":
                campus_cafe.show_report()
            case "4":
                show_stock(campus_cafe.stock)
            case "5":
                for _ in range(3):
                    print("Closing")
                running = False
            case _:
                print("Invalid choice.")


print("=== CUSTOMER ANALYSIS ===")
analyze_customers(daily_customer_counts)

print("\nDictionary keys:", stock.keys())
print("Dictionary values:", stock.values())

run_cafe()


#This is update of codebase performed by PwP_Instructor
#This is another update of codebase performed by PwP_Instructor

#This is update of codebase performed by PwP_Instructor - this is in branch "new_feature"
#This is another update of codebase performed by PwP_Instructor - this is in branch "new_feature"