class Client:
    def __init__(self, client_id, full_name, contact_info):
        self.client_id = client_id
        self.full_name = full_name
        self.contact_info = contact_info

    def __str__(self):
        return f"ID клиента: {self.client_id}, ФИО клиента: {self.full_name}, Контактные данные: {self.contact_info}"
