import json

def task() -> float:
    # Открываем JSON файл и загружаем его содержимое
    with open('input.json', 'r') as file:
        data = json.load(file)
    # задаем переменную для подсчета суммы
    total_sum = 0.0
    # проходим по каждому элементу в списке
    for entry in data:
        score = entry.get('score', 0)
        weight = entry.get('weight', 0)

        total_sum += score * weight

    return round(total_sum, 3)

print(task())