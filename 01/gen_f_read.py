def gen(file, words):
    if isinstance(file, str):
        file = open(file, "r")
    for line in file:
        flag = False
        for word in line.split():
            for i in words:
                if (word.lower() == i.lower() and not (flag)):
                    flag = True
                    yield line
    file.close()
