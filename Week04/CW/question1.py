name_input = input("enter names ")

name_list = name_input.split(',')

#print(name_list)

filtered_name = sorted([ name for name in name_list  if len(name) > 3 and name[0].lower() == "a" ])

with open('name.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(filtered_name))
    file.write(f"\nCount: {len(filtered_name)}")

print(f"File saved successfully with {len(filtered_name)} names.")