def max_distance(input_list):

    max_val = int(max(input_list))
    min_val = int(min(input_list))

    print(max_val - min_val)

input_list = list(input("Please enter the list : "))
max_distance(input_list)