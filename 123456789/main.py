from client import Client
from product import Product
from order import Order
from receipt import Receipt
from order_proces import OrderProces


def main():
    order_processing_system = OrderProces()

    while True:
        print("------- МЕНЮ ------")
        print("1. Добавить клиента")
        print("2. Добавить товар")
        print("3. Оформить заказ")
        print("4. Сгенерировать чек")
        print("5. Вывести товары в наличии")
        print("6. Вывести сумму проданных товаров")
        print("7. Вывести самый большой заказ")
        print("8. Выход")

        choice = input("Введите номер опции: ")

        if choice == "1":
            client_id = input("Введите ID клиента: ")
            full_name = input("Введите ФИО клиента: ")
            contact_info = input("Введите контактные данные клиента: ")
            client = Client(client_id, full_name, contact_info)
            order_processing_system.add_client(client)
            print(client)

        elif choice == "2":
            product_id = input("Введите ID товара: ")
            name = input("Введите название товара: ")
            price = input("Введите цену товара: ")
            availability = input("Введите наличие товара: ")
            weight = input("Введите вес товара: ")
            product = Product(product_id, name, price, availability, weight)
            order_processing_system.add_product(product)
            print(product)

        elif choice == "3":
            order_id = input("Введите ID заказа: ")
            product_ids = input("Введите ID товаров через запятую: ").split(',')
            delivery_location = input("Введите место доставки: ")
            payment_method = input("Введите способ оплаты: ")
            contact_info = input("Введите контактные данные: ")
            total_amount = input("Введите сумму заказа: ")
            order = Order(order_id, product_ids, delivery_location, payment_method, contact_info, total_amount)
            order_processing_system.place_order(order)
            print(order)

        elif choice == "4":
            receipt_id = input("Введите ID чека: ")
            num_of_items = input("Введите количество товаров в чеке: ")
            order_id = input("Введите ID заказа, к которому привязан чек: ")
            total_amount = input("Введите сумму товаров в чеке: ")
            receipt = Receipt(receipt_id, num_of_items, order_id, total_amount)
            order_processing_system.generate_receipt(receipt)
            print(receipt)

        elif choice == "5":

            available_products = order_processing_system.get_available_products()

            print("Товары в наличии:")

            for product in available_products:
                print(f"ID товара: {product.product_id}, Название: {product.name}, Цена: {product.price}")

        elif choice == "6":

            total_sales_amount = order_processing_system.get_total_sales_amount()

            print(f"Сумма проданных товаров: {total_sales_amount}")

        elif choice == "7":

            largest_order = order_processing_system.get_largest_order()

            if largest_order:
                print("Самый большой заказ:")

                print(f"ID заказа: {largest_order.order_id}, Сумма заказа: {largest_order.total_amount}")

        elif choice == "8":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите существующую опцию.")


if __name__ == "__main__":
    main()
