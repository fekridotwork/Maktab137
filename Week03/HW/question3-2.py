# Quick sort

def partition(lis, start_index, end_index):

    # choose last element of the list as pivot
    pivot = lis[end_index]

    # pointer for smaller elements
    smaller_index = start_index - 1 #empty

    for current_index in range(start_index, end_index):
        if lis[current_index] <= pivot:
            smaller_index += 1
            lis[smaller_index], lis[current_index] = lis[current_index], lis[smaller_index]

    lis[smaller_index + 1], lis[end_index] = lis[end_index], lis[smaller_index + 1]
    return smaller_index + 1

# main function
def quick_sort(lis, start_index, end_index):
    if start_index < end_index:
        pivot_index = partition(lis, start_index, end_index)
        quick_sort(lis, start_index, pivot_index - 1)
        quick_sort(lis, pivot_index + 1, end_index)


input_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

quick_sort(input_list, 0, len(input_list) - 1)

print(f"The sorted list is :\n{input_list}")
