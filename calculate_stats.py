def calculate_statistics(*data):
    if not data:
        print("Вызовите функцию повторно и введите хотя бы один аргумент!")
        return None
    data_dictionary = {
            "Максимум" : max(data),
            "Минимум": min(data),
            "Сумма" : sum(data),
            "Среднее" : (sum(data) / len(data))
            }
    return data_dictionary