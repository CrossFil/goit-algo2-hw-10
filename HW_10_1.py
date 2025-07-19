import random
import time
import matplotlib.pyplot as plt


def randomized_quick_sort(arr):
    """Рандомізований QuickSort з випадковим вибором опорного елемента"""
    if len(arr) <= 1:
        return arr

    # Випадковий вибір опорного елемента
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    # Розділення масиву
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Рекурсивне сортування
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    """Детермінований QuickSort з фіксованим вибором опорного елемента (перший)"""
    if len(arr) <= 1:
        return arr

    # Фіксований вибір опорного елемента (перший)
    pivot = arr[0]

    # Розділення масиву
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Рекурсивне сортування
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


def measure_time(sort_function, arr, runs=5):
    """Вимірює середній час виконання функції сортування"""
    total_time = 0

    for _ in range(runs):
        arr_copy = arr.copy()
        start_time = time.time()
        sort_function(arr_copy)
        end_time = time.time()
        total_time += (end_time - start_time)

    return total_time / runs


def create_test_arrays():
    """Створює тестові масиви різного розміру"""
    sizes = [10000, 50000, 100000, 500000]
    arrays = {}

    for size in sizes:
        arrays[size] = [random.randint(1, 10000) for _ in range(size)]

    return arrays


def run_comparison():
    """Проводить порівняльний аналіз алгоритмів"""
    # Створення тестових масивів
    test_arrays = create_test_arrays()

    # Результати
    sizes = []
    randomized_times = []
    deterministic_times = []

    print("Порівняння рандомізованого та детермінованого QuickSort:")
    print("=" * 60)

    for size, arr in test_arrays.items():
        print(f"\nРозмір масиву: {size}")

        # Вимірювання часу для рандомізованого QuickSort
        rand_time = measure_time(randomized_quick_sort, arr)
        print(f"   Рандомізований QuickSort: {rand_time:.4f} секунд")

        # Вимірювання часу для детермінованого QuickSort
        det_time = measure_time(deterministic_quick_sort, arr)
        print(f"   Детермінований QuickSort: {det_time:.4f} секунд")

        # Збереження результатів
        sizes.append(size)
        randomized_times.append(rand_time)
        deterministic_times.append(det_time)

    # Побудова графіка
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, randomized_times, 'o-', label='Рандомізований QuickSort', linewidth=2, markersize=8)
    plt.plot(sizes, deterministic_times, 's-', label='Детермінований QuickSort', linewidth=2, markersize=8)

    plt.xlabel('Розмір масиву', fontsize=12)
    plt.ylabel('Час виконання (секунди)', fontsize=12)
    plt.title('Порівняння ефективності алгоритмів QuickSort', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    # Форматування осей
    plt.ticklabel_format(style='plain', axis='x')

    plt.show()

    # Аналіз результатів
    print("\n" + "=" * 60)
    print("АНАЛІЗ РЕЗУЛЬТАТІВ:")
    print("=" * 60)

    # Таблиця результатів
    print(f"{'Розмір масиву':<15} {'Рандомізований':<18} {'Детермінований':<18} {'Різниця (%)':<12}")
    print("-" * 65)

    for i, size in enumerate(sizes):
        diff_percent = ((deterministic_times[i] - randomized_times[i]) / randomized_times[i]) * 100
        print(f"{size:<15} {randomized_times[i]:<18.4f} {deterministic_times[i]:<18.4f} {diff_percent:<12.2f}")

    # Висновки
    avg_rand = sum(randomized_times) / len(randomized_times)
    avg_det = sum(deterministic_times) / len(deterministic_times)

    print(f"\nСередній час виконання:")
    print(f"  Рандомізований QuickSort: {avg_rand:.4f} секунд")
    print(f"  Детермінований QuickSort: {avg_det:.4f} секунд")

    if avg_rand < avg_det:
        faster = "рандомізований"
        improvement = ((avg_det - avg_rand) / avg_det) * 100
    else:
        faster = "детермінований"
        improvement = ((avg_rand - avg_det) / avg_rand) * 100

    print(f"\nВИСНОВКИ:")
    print(f"• {faster.capitalize()} QuickSort в середньому швидший на {improvement:.2f}%")
    print(f"• Рандомізований QuickSort має кращу стабільність через уникнення найгірших випадків")
    print(f"• На випадкових даних обидва алгоритми показують схожу ефективність O(n log n)")
    print(f"• Детермінований QuickSort може деградувати до O(n²) на відсортованих масивах")


if __name__ == "__main__":
    # Встановлення seed для відтворюваності результатів
    random.seed(42)

    # Запуск порівняльного аналізу
    run_comparison()

    # ============================================================
    # Порівняння рандомізованого та детермінованого QuickSort:
    # ============================================================

    # Розмір масиву: 10000
    #    Рандомізований QuickSort: 0.0421 секунд
    #    Детермінований QuickSort: 0.0361 секунд

    # Розмір масиву: 50000
    #    Рандомізований QuickSort: 0.1865 секунд
    #    Детермінований QuickSort: 0.1808 секунд

    # Розмір масиву: 100000
    #    Рандомізований QuickSort: 0.4272 секунд
    #    Детермінований QuickSort: 0.3092 секунд

    # Розмір масиву: 500000
    #    Рандомізований QuickSort: 1.3317 секунд
    #    Детермінований QuickSort: 1.1499 секунд

    # ============================================================
    # АНАЛІЗ РЕЗУЛЬТАТІВ:
    # ============================================================
    # Розмір масиву   Рандомізований     Детермінований     Різниця (%)
    # -----------------------------------------------------------------
    # 10000           0.0421             0.0361             -14.07
    # 50000           0.1865             0.1808             -3.06
    # 100000          0.4272             0.3092             -27.62
    # 500000          1.3317             1.1499             -13.66

    # Середній час виконання:
    #   Рандомізований QuickSort: 0.4969 секунд
    #   Детермінований QuickSort: 0.4190 секунд

    # ВИСНОВКИ:
    # • Детермінований QuickSort в середньому швидший на 15.67%
    # • Рандомізований QuickSort має кращу стабільність через уникнення найгірших випадків
    # • На випадкових даних обидва алгоритми показують схожу ефективність O(n log n)
    # • Детермінований QuickSort може деградувати до O(n²) на відсортованих масивах
