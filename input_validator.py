class InputValidator:
    @staticmethod
    def validate_date(date):
        # Простая валидация даты, должен быть формат ГГГГ-ММ-ДД
        return len(date) == 10 and date[4] == date[7] == '-' and date[:4].isdigit() and date[5:7].isdigit() and date[
                                                                                                                8:].isdigit()

    @staticmethod
    def validate_category(category):
        return category in ["Доход", "Расход"]

    @staticmethod
    def validate_amount(amount):
        try:
            amount = float(amount)
            return amount > 0
        except ValueError:
            return False
