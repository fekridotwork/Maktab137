filename = "sample.txt"

with open(filename, "w") as f:
    f.write("Hello\n")
    f.write("This is a test\n")
    f.write("Using python\n")

with open(filename, "r") as f:
    for line in f:
        print(line.strip())
