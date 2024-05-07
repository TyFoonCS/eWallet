import os


class Wallet:
    def __init__(self, data_file):
        self.data_file = data_file
        self.records = self.read_data()

    def read_data(self):
        if not os.path.exists(self.data_file):
            return []
        with open(self.data_file, "r") as file:
            lines = file.readlines()
        records = []
        record = {}
        for line in lines:
            line = line.strip()
            if line:
                key, value = line.split(": ")
                record[key] = value
            else:
                records.append(record)
                record = {}
        return records

    def write_data(self):
        with open(self.data_file, "w") as file:
            for record in self.records:
                for key, value in record.items():
                    file.write(f"{key}: {value}\n")
                file.write("\n")

    def show_balance(self):
        income = sum(float(record["Сумма"]) for record in self.records if record["Категория"] == "Доход")
        expenses = sum(float(record["Сумма"]) for record in self.records if record["Категория"] == "Расход")
        balance = income - expenses
        print(f"Текущий баланс: {balance}")
        print(f"Доходы: {income}")
        print(f"Расходы: {expenses}")

    def add_record(self, record):
        self.records.append(record)
        self.write_data()

    def edit_record(self, index, field, new_value):
        record = self.records[index]
        record[field] = new_value
        self.write_data()
        print("Запись успешно отредактирована.")

    def search_records(self, category=None, date=None, amount=None):
        found_records = []
        for record in self.records:
            if (not category or record["Категория"] == category) and \
                    (not date or record["Дата"] == date) and \
                    (not amount or record["Сумма"] == amount):
                found_records.append(record)
        return found_records

    def show_records(self, records=None):
        records = records or self.records
        for i, record in enumerate(records, start=1):
            print(f"Запись {i}:")
            for key, value in record.items():
                print(f"{key}: {value}")
            print()
