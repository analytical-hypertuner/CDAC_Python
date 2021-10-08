# File Address
# 7. Write a Python program to read an entire text file.

actual = "D:\\PG-DAI\\LAB\\Lab 6\\mypkg\\new.txt"


def readFile():
    with open(actual) as file:
        for line in file:
            print(line)


readFile()


# 8.  Write a Python program to read the first n lines of a file.
def first_n(filepath):
    with open(filepath) as file:
        n = int(input("Enter the lines you need: "))
        # while n > 0:
        for line in file:
            if n > 0:
                print(line)
                n = n - 1


first_n(actual)

# Function to print file content
def readFilex(actual):
    with open(actual, 'r') as file:
        print(file.readlines())


readFilex(actual)

# 9. Write a Python program to append text to a file and display the text.

def appendlines(filepath):
    with open(filepath, 'a') as file:
        # lines_content = file.readlines()
        # print(lines_content)
        # print("Content before appending.")
        file.write(" \nThis is added content")
        print("Appending finished")
        return


appendlines(actual)

# Function to print file content
readFilex(actual)
lineList = []


# 10. Write a Python program to read a file line by line and store it into a list.
def readLineBline(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            lineList.append(line)
    print(type(lineList))
    return lineList


readLineBline(actual)

# 11.  Write a program to print each line of a file in reverse order.
print(lineList, ": This is a List")
print(type(lineList))

lineList.reverse()
print(lineList, "Reversed list by line")

# 12. Write a Python program to write a list content to a file.

list_2_append = ['this', 'is', 'an', 'appended', 'list']


def appendlist(filepath, list_2_):
    with open(filepath, 'a') as file:
        for x in list_2_:
            file.write("\n" + x)
            print("Appending list done", str(x))
        print(lineList)


appendlist(actual, list_2_append)

# 13. Write a program to compute the number of characters, words and lines in a file.
def countLines(filepath):
    name = open(filepath, 'r')

    lines_content = name.read()
    line_c = 1 + lines_content.count("\n")

    print("Function print lines count: ", line_c)
    return line_c


import re


#
# def countWords(filepath):
#     list_noun = []
#     name = open(filepath, 'r')
#     print(name)
#     for word in name:
#         x = word.split(" ")
#         for y in x:
#             y.split("\n")
#         print(y)
#         list_noun.append(y)
#         print(list_noun)
#         print(len(list_noun))
# # word = name.read().split("\n")
# a=" "
# re.split(',|\n',name)
# len_words = sum(len(noun) for noun in word)
# count = 0
# for noun in word:
#     print(noun)
#     list_noun.append(noun)
# print(list_noun)
#         #count = count+1
#     list_noun.append(noun)
# print("Number of words: ",len(list_noun.split('\n')))
# print("list noun:", )
# print("Function print Words: ", len(list_noun))
# print(count,"WOrds")
# print(word)

def countWords(filepath):
    name = open(filepath, 'r')
    counter = 0
    a = name.read().split()
    for x in a:
        str(x).split("\n")

    print("Number of words: ", len(a))


def countChars(filepath):
    name = open(filepath, 'r')
    text = name.read().split()
    len_chars = sum(len(word) for word in text)
    # print (len_chars)
    print("Function print Chars: ", len_chars)
    return len_chars


countLines(actual)
countWords(actual)
countChars(actual)
