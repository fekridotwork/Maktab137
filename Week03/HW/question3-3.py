# Merge sort

def merge(array, left_index, middle_index, right_index):

    # calculating sizes of two subarrays
    left_size = middle_index - left_index + 1
    right_size = right_index - middle_index

    # Create temp arrays
    left_part = [0] * left_size
    right_part = [0] * right_size

    # Coping data from main array to temp arrays
    for i in range(0, left_size):
        left_part[i] = array[left_index + i]

    for j in range(0, right_size):
        right_part[j] = array[middle_index + 1 + j]

    
    left_pointer = 0     
    right_pointer = 0    
    merge_pointer = left_index  

    # Merge the temp arrays back into array[left_index..right_index]
    while left_pointer < left_size and right_pointer < right_size:
        if left_part[left_pointer] <= right_part[right_pointer]:
            array[merge_pointer] = left_part[left_pointer]
            left_pointer += 1
        else:
            array[merge_pointer] = right_part[right_pointer]
            right_pointer += 1
        merge_pointer += 1

    # Copy the remaining elements of left_part 
    while left_pointer < left_size:
        array[merge_pointer] = left_part[left_pointer]
        left_pointer += 1
        merge_pointer += 1

    # Copy the remaining elements of right_part 
    while right_pointer < right_size:
        array[merge_pointer] = right_part[right_pointer]
        right_pointer += 1
        merge_pointer += 1

# Main function
def merge_sort(input_list, left_start, right_end):

    #check for single member list
    if left_start < right_end:

        # finding the middle element of the list
        middle = (left_start + right_end) // 2

        # Sorting the left sublist
        merge_sort(input_list, left_start, middle)

        # Sorting the right sublist
        merge_sort(input_list, middle + 1, right_end)

        # Merging the two sorted sub-lists
        merge(input_list, left_start, middle, right_end)


# Getting the list from the user
input_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Process and printing the sorted list
merge_sort(input_list, 0, len(input_list) - 1)
print(f"The sorted list is :\n{input_list}")