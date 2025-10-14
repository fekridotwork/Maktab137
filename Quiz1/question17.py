def reverse(dictionary: dict):
    output_dict = {}
    for key, val in dictionary.items():
        if val not in output_dict:
            output_dict[val] = []
        output_dict[val].append(key)
    # For 1 item keys returning the item itself not in list
    for val in output_dict:
        if len(output_dict[val]) == 1:
            output_dict[val] = output_dict[val][0]
    return output_dict

input_dict = {
"apple": "fruit",
"banana": "fruit",
"carrot": "vegetable",
"tomato": "vegetable",
"laptop": "technology"
}
result = reverse(input_dict)
print(result)
