# main.py
import sys

from variant1_mod import extract_top_vibes, filter_outliers, get_stat_dict


def main():
    max_limit = float(sys.argv[1]) if len(sys.argv) > 1 else 45.0

    raw_sensor_data = [12.4, 15.1, -99.0, 18.2, 520.0, 22.0, 41.5, 14.8, 48.0, 19.3]

    clean_data = filter_outliers(raw_sensor_data, min_val=0.0, max_val=max_limit)
    stats = get_stat_dict(clean_data)
    
    recent_samples = clean_data[-3:]

    print(f"=== ВИБРОДИАГНОСТИКА ПОДШИПНИКОВ ({sys.argv[0]}) ===")
    print(f"Предел фильтрации (sys.argv): {max_limit} мм/с")
    print(f"Очищенная выборка: {clean_data}")
    print(f"Последние 3 замера (срез): {recent_samples}")
    
    print("Статистика:")
    for key, val in stats.items():
        print(f"  - {key}: {val}")

    top_vibes = extract_top_vibes(clean_data, k=3)
    print(f"ТОП-3 критических пика (срез [:3]): {top_vibes}")

if __name__ == '__main__':
    main()