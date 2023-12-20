class Order:
    def __init__(self, order_id, product_ids, delivery_location, payment_method, contact_info, total_amount):
        self.order_id = order_id
        self.product_ids = product_ids
        self.delivery_location = delivery_location
        self.payment_method = payment_method
        self.contact_info = contact_info
        self.total_amount = total_amount

    def __str__(self):
        return f"ID заказа: {self.order_id}, ID продукта: {self.product_ids}, Место доставки: {self.delivery_location}, Способ оплаты: {self.payment_method}, Контактные данные: {self.contact_info}, Сумма заказа: {self.total_amount}"

