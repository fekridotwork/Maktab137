def check_input(x):
    if type(x) == int:
        return x ** 2
    elif type(x) == str:
        return len(x)
    elif type(x) == list:
        return sum(x)
