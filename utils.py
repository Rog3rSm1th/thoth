OPERATORS = {"ADD" : "+", "MUL" : "*"}
PRIME = (2**251) + (17 * (2**192)) + 1

def format_print(data, end="\n"):
    spaces = " " * 15
    print(data + spaces[len(data):], end=end)
