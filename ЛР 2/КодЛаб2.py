# lab2_variant1.py
# Лабораторная работа №2. Вариант 1: Моделирование реактора

def analyze_reactor(temperatures, norm_temp=100, max_temp=180):
    """
    Анализирует список замеров температур реактора.
    Выводит статус для каждого замера и рассчитывает итоговые метрики.
    
    :param temperatures: список (list) вещественных чисел (замеры температур)
    :param norm_temp: нижняя граница нормы (по умолчанию 100)
    :param max_temp: верхняя граница нормы / аварийный порог (по умолчанию 180)
    :return: кортеж (средняя температура, количество аварийных замеров)
    """
    if not temperatures:
        return 0.0, 0
        
    total_temp = 0
    emergency_count = 0
    
    print("--- Пошаговый анализ замеров ---")
    for idx, t in enumerate(temperatures, start=1):
        total_temp += t
        
        # Ветвление согласно условию задачи
        if t < norm_temp:
            status = "Нагрев"
        elif norm_temp <= t <= max_temp:
            status = "Норма"
        else:
            status = "Авария"
            emergency_count += 1
            
        print(f"Замер №{idx}: {t:.1f}°C -> Статус: [{status}]")
        
    # Расчет средней температуры
    avg_temp = total_temp / len(temperatures)
    
    return avg_temp, emergency_count


# Основной блок программы (тестирование функции)
if __name__ == "__main__":
    print("=== ЛАБОРАТОРНАЯ РАБОТА №2: МОДЕЛИРОВАНИЕ РЕАКТОРА ===\n")
    
    # Тестовый набор данных №1 (разнородные параметры)
    test_data_1 = [85.5, 120.0, 195.3, 99.0, 150.2, 210.0]
    print("ТЕСТ №1")
    avg_1, emergency_1 = analyze_reactor(test_data_1)
    print("\nРезультат теста №1:")
    print(f"Средняя температура: {avg_1:.2f}°C")
    print(f"Количество аварийных замеров: {emergency_1}")
    print("-" * 40 + "\n")
    
    # Тестовый набор данных №2 (все в норме)
    test_data_2 = [105.0, 140.5, 175.0]
    print("ТЕСТ №2")
    avg_2, emergency_2 = analyze_reactor(test_data_2)
    print("\nРезультат теста №2:")
    print(f"Средняя температура: {avg_2:.2f}°C")
    print(f"Количество аварийных замеров: {emergency_2}")
    print("-" * 40)
