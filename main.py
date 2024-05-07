import sys
from wallet import Wallet
from input_validator import InputValidator


def main():
    wallet = Wallet("finances.txt")
    while True:
        print("\nВыберите действие:")
        print("1. Вывод баланса")
        print("2. Добавление записи")
        print("3. Редактирование записи")
        print("4. Поиск по записям")
        print("5. Вывод всех записей")
        print("6. Выход")
        choice = input("Ваш выбор: ")

        if choice == "1":
            wallet.show_balance()
        elif choice == "2":
            record = {
                "Дата": "",
                "Категория": "",
                "Сумма": "",
                "Описание": ""
            }
            while not InputValidator.validate_date(record["Дата"]):
                record["Дата"] = input("Введите дату (гггг-мм-дд): ")
            while not InputValidator.validate_category(record["Категория"]):
                record["Категория"] = input("Введите категорию (Доход/Расход): ")
            while not InputValidator.validate_amount(record["Сумма"]):
                record["Сумма"] = input("Введите сумму: ")
            record["Описание"] = input("Введите описание: ")
            wallet.add_record(record)
            print("Запись успешно добавлена.")
        elif choice == "3":
            wallet.show_records()
            index = int(input("Введите номер записи для редактирования: ")) - 1
            fields = list(wallet.records[index].keys())
            print("Выберите поле для редактирования:")
            for i, field in enumerate(fields, start=1):
                print(f"{i}. {field}")
            while True:
                try:
                    choice_field = int(input("Ваш выбор: "))
                    if 1 <= choice_field <= len(fields):
                        break
                    else:
                        print("Некорректный выбор. Повторите ввод.")
                except ValueError:
                    print("Некорректный ввод. Введите число.")
            field = fields[choice_field - 1]
            new_value = input("Введите новое значение: ")
            wallet.edit_record(index, field, new_value)
        elif choice == "4":
            category = input("Введите категорию для поиска (Доход/Расход): ")
            date = input("Введите дату для поиска (гггг-мм-дд): ")
            amount = input("Введите сумму для поиска: ")
            found_records = wallet.search_records(category, date, amount)
            if found_records:
                print("Найденные записи:")
                wallet.show_records(found_records)
            else:
                print("Записи не найдены.")
        elif choice == "5":
            wallet.show_records()
        elif choice == "6":
            sys.exit("До свидания!")
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
