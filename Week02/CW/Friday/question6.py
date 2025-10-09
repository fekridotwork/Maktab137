count = 0

with open(r'Sample.txt','r') as f:
    data = f.read()
    words = data.split()
    count += len(words)

print(count)