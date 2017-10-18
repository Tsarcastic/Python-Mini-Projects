def remove_smallest(numbers):
    def remove_smallest(numbers):
    if numbers:
        the_min = min(numbers)
        numbers.remove(the_min)
    return numbers

print(remove_smallest([9, 8, 1, 2]))