def digit_sort(numbers: list) -> list:
    def digit_sum(num):
        sum = 0
        for digit in str(num):
            sum += int(digit)
        return sum
    # Sort with tuple for equal sum-digit cases
    sorted_list = sorted(numbers, key = lambda x : (digit_sum(x), x)) 
    return sorted_list

numbers = list(input("Please enter your list of numbers: ").split())
result = digit_sort(numbers)
print(result)