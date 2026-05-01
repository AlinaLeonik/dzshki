some_list = ["abba", "asesa", "asdf", "fghgf", "qwerty"]

print(list(filter(lambda x: x == x[::-1], some_list)))
