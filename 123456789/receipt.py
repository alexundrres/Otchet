class Receipt:
    def __init__(self, receipt_id, num_of_items, order_id, total_amount):
        self.receipt_id = receipt_id
        self.num_of_items = num_of_items
        self.order_id = order_id
        self.total_amount = total_amount

    def __str__(self):
        return f"ID чека: {self.receipt_id}, Количество товаров: {self.num_of_items}, ID заказа: {self.order_id}, Сумма заказа: {self.total_amount}"
