# variant1_mod.py

def filter_outliers(vibe_list, min_val=0.0, max_val=50.0):
    cleaned = [x for x in vibe_list if min_val <= x <= max_val]
    return cleaned

def get_stat_dict(vibe_list):
    if not vibe_list:
        return {'count': 0, 'mean': 0.0, 'min': 0.0, 'max': 0.0}
    
    mean_val = sum(vibe_list) / len(vibe_list)
    
    return {
        'count': len(vibe_list),
        'mean': round(mean_val, 3),
        'min': min(vibe_list),
        'max': max(vibe_list)
    }

def extract_top_vibes(vibe_list, k=3):
    sorted_vibes = sorted(vibe_list, reverse=True)
    top_k = sorted_vibes[:k]
    return top_k

if __name__ == '__main__':
    # Блок автономного тестирования модуля
    test_raw = [12.4, 15.1, -99.0, 18.2, 520.0]
    filtered = filter_outliers(test_raw, 0.0, 50.0)
    stats = get_stat_dict(filtered)
    top_vibes = extract_top_vibes(filtered, k=3)
    
    print(f"[Автотест модуля] Отфильтрованный сигнал: {filtered}")
    print(f"[Автотест модуля] Статистика: {stats}")
    print(f"[Автотест модуля] ТОП-3 пика: {top_vibes}")