# Bubble sort
def bubble_sort(unsorted_list: list):

    # Calculating length of the list
    n = len(unsorted_list)

    # Iterate over the list
    for i in range(n - 1):

        sorted = True

        for j in range(n - i - 1):

            if unsorted_list[j + 1] < unsorted_list[j]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                
                sorted = False

        if sorted:
            break

    print(unsorted_list)            

input_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
bubble_sort(input_list)