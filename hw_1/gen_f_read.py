def gen(file_name, a):
    for line in open(file_name, "r"):
        flag = False
        for word in line.split():
            for i in a:
                if (word.lower() == i.lower() and not (flag)):
                    flag = True
                    yield line
