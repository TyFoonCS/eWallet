# Учет личных доходов и расходов

Программа представляет собой простой инструмент для учета личных финансов. Она позволяет пользователям записывать свои доходы и расходы, просматривать текущий баланс, редактировать и искать записи.

## Основные возможности

1. **Вывод баланса:** Показывает текущий баланс, а также отдельно доходы и расходы.
2. **Добавление записи:** Позволяет добавить новую запись о доходе или расходе.
3. **Редактирование записи:** Позволяет изменить существующие записи о доходах и расходах.
4. **Поиск по записям:** Позволяет найти записи по категории, дате или сумме.

## Схема

1. **Интерфейс:** Реализован через консольный интерфейс (CLI), без использования веб- или графического интерфейса.
2. **Хранение данных:** Данные хранятся в текстовом файле.
3. **Информация в записях:** Каждая запись содержит дату, категорию (доход/расход), сумму и описание.

## Как использовать

1. **Запуск программы:** Запустите файл `main.py` для начала работы с программой.
2. **Выбор действий:** Программа предложит вам выбрать действие из списка.
3. **Действия:**
   - Вывод баланса
   - Добавление записи
   - Редактирование записи
   - Поиск по записям
   - Вывод всех записей
   - Выход

## Примеры использования

1. **Добавление записи:**
   - Выберите "Добавление записи" из меню.
   - Введите дату, категорию, сумму и описание записи.
   - Запись будет добавлена в файл с данными.

2. **Редактирование записи:**
   - Выберите "Редактирование записи" из меню.
   - Выберите запись, которую хотите отредактировать, и поле для редактирования.
   - Введите новое значение поля.
   - Запись будет изменена в файле с данными.

3. **Поиск по записям:**
   - Выберите "Поиск по записям" из меню.
   - Введите параметры поиска (категорию, дату или сумму).
   - Найденные записи будут выведены на экран.

4. **Вывод всех записей:**
   - Выберите "Вывод всех записей" из меню.
   - Все записи будут выведены на экран.

5. **Выход:**
   - Выберите "Выход" из меню, чтобы завершить программу.

## Требования к среде выполнения

- Python 3.x