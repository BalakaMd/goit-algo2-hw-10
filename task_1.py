import random
import time
import matplotlib.pyplot as plt


# Рандомізований QuickSort: вибір опорного елемента випадковим чином
def randomized_quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


# Детермінований QuickSort: вибір опорного елемента як середній елемент
def deterministic_quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


# Функція для вимірювання часу виконання сортування
def measure_time(sort_function, arr):
    start = time.perf_counter()
    sort_function(arr)
    end = time.perf_counter()
    return end - start


array_sizes = [10000, 50000, 100000, 500000]

randomized_times = []
deterministic_times = []

runs = 5

# Проведення тестування для кожного розміру масиву
for size in array_sizes:
    # Генерація масиву випадкових чисел
    test_array = [random.randint(0, 1000000) for _ in range(size)]

    times_random = []
    times_det = []

    # Вимірювання часу для рандомізованого QuickSort
    for _ in range(runs):
        arr_copy = test_array[:]  # копія масиву для коректного вимірювання
        t = measure_time(randomized_quick_sort, arr_copy)
        times_random.append(t)
    avg_random = sum(times_random) / runs
    randomized_times.append(avg_random)

    # Вимірювання часу для детермінованого QuickSort
    for _ in range(runs):
        arr_copy = test_array[:]
        t = measure_time(deterministic_quick_sort, arr_copy)
        times_det.append(t)
    avg_det = sum(times_det) / runs
    deterministic_times.append(avg_det)

    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {avg_random:.4f} секунд")
    print(f"   Детермінований QuickSort: {avg_det:.4f} секунд")
    print()

# Побудова графіка для порівняння часу виконання
plt.figure(figsize=(10, 6))
plt.plot(array_sizes, randomized_times, marker='o', label='Рандомізований QuickSort')
plt.plot(array_sizes, deterministic_times, marker='o', label='Детермінований QuickSort')
plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (секунди)")
plt.title("Порівняльний аналіз QuickSort")
plt.legend()
plt.grid(True)
plt.show()
