import random

# =========================
# SORTING ALGORITHMS
# =========================

print("REMOTE VERSION - GitHub changed this file")

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# =========================
# SEARCH ALGORITHMS
# =========================

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# =========================
# MAIN PROGRAM
# =========================

print("=== RANDOM NUMBER SORT & SEARCH SYSTEM ===")

# Step 1: Generate numbers
count = int(input("How many random numbers do you want to generate? "))
numbers = [random.randint(1, 100) for _ in range(count)]

print("\nGenerated Numbers:")
print(numbers)

# Step 2: Choose sorting
print("\nChoose sorting method:")
print("1. Bubble Sort")
print("2. Selection Sort")
print("3. Insertion Sort")

sort_choice = input("Enter choice (1-3): ")

if sort_choice == "1":
    numbers = bubble_sort(numbers)
    print("\nSorted using Bubble Sort")
elif sort_choice == "2":
    numbers = selection_sort(numbers)
    print("\nSorted using Selection Sort")
elif sort_choice == "3":
    numbers = insertion_sort(numbers)
    print("\nSorted using Insertion Sort")
else:
    print("Invalid choice, defaulting to Bubble Sort")
    numbers = bubble_sort(numbers)

print(numbers)

# Step 3: Choose search
print("\nChoose search method:")
print("1. Linear Search")
print("2. Binary Search")

search_choice = input("Enter choice (1-2): ")

target = int(input("Enter number to search for: "))

if search_choice == "1":
    index = linear_search(numbers, target)
    method = "Linear Search"
elif search_choice == "2":
    index = binary_search(numbers, target)
    method = "Binary Search"
else:
    print("Invalid choice, using Linear Search")
    index = linear_search(numbers, target)
    method = "Linear Search"

# Step 4: Result
print(f"\nUsing {method}")

if index != -1:
    print(f"Number found at index {index}")
else:
    print("Number not found")
