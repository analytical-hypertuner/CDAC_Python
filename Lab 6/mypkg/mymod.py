import os


# filepath = "D:\\PG-DAI\\LAB\\Lab 6\\new.txt"

def countLines(filepath):
    name = open(filepath, 'r')

    lines_content = name.read()
    line_c = 1 + lines_content.count("\n")

    print("Function print lines count: ", line_c)
    return line_c


def countChars(filepath):
    name = open(filepath, 'r')
    text = name.read().split()
    len_chars = sum(len(word) for word in text)
    # print (len_chars)
    print("Function print Chars: ", len_chars)
    return len_chars


actual = "D:\\PG-DAI\\LAB\\Lab 6\\mypkg\\new.txt"


def test(filepathx):
    print("The number of chars are: ", countChars(filepathx))
    print("The number of lines are: ", countLines(filepathx))


print("Main MyMod file, import successfully completed!")

x = "__main__"

if (__name__ == x):
    test(actual)
