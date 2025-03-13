import random


def filter_below_ten(num):
    if num < 10:
        return num


rand_list = [random.randint(1, 20) for i in range(10)]
print(f"Create a list of 10 random numbers between 1 and 20: {rand_list}")

list_comprehension_below_10 = [num for num in rand_list if num < 10]
print(f"Filter Numbers Below 10 (List Comprehension): {list_comprehension_below_10}")

list_comprehension_below_10_with_filter = list(filter(filter_below_ten, rand_list))
print(f"Filter Numbers Below 10 (Using filter): {list_comprehension_below_10_with_filter}")