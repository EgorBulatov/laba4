import csv  # Для работы с CSV файлами
import json  # Для работы с JSON файлами


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, newline='', encoding='utf-8') as input_f:
        # Читаем CSV файл с разделителем по умолчанию (',') и строками по умолчанию (\n)
        reader = csv.DictReader(input_f, delimiter=',')

        # Преобразуем все строки CSV в список словарей, где ключи — это имена столбцов
        data = [row for row in reader]

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as output_f:
        json.dump(data, output_f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
