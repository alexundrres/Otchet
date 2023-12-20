from client import Client
from product import Product


class OrderProces:
    def __init__(self):
        self.clients = []
        self.products = []
        self.orders = []
        self.receipts = []

    def add_client(self, client):
        self.clients.append(client)

    def add_product(self, product):
        self.products.append(product)

    def load_clients_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(';')
                client = Client(data[0], data[1], data[2])
                self.add_client(client)

    def load_products_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(';')
                product = Product(data[0], data[1], data[2], data[3], data[4])
                self.add_product(product)

    def place_order(self, order):
        self.orders.append(order)

    def generate_receipt(self, receipt):
        self.receipts.append(receipt)

    def get_available_products(self):
        return [product for product in self.products if product.availability == 'Есть в наличии']

    def get_total_sales_amount(self):
        return sum(float(order.total_amount) for order in self.orders)

    def get_largest_order(self):
        if not self.orders:
            print("Нет доступных заказов.")
            return None
        return max(self.orders, key=lambda order: float(order.total_amount))