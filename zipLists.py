# -*- coding: utf-8 -*-
"""
input:
List1, List2

length of list is: list1 = list2

output:

for each element

(list1[i] = List2[i])*

"""

input_left = "C:/Temp/ablkeywords_notcomplete.txt"
input_right = "C:/Temp/ablkeywords_notcomplete_komma.txt"

with open(input_left, 'r', encoding="ANSI") as txt:
    program_txt1 = txt.read()
with open(input_right, 'r', encoding="ANSI") as txt:
    program_txt2 = txt.read()


program_txt1 = program_txt1.split(',')
program_txt2 = program_txt2.split(',')

a_zip = zip(program_txt1, program_txt2)

zipped_list = list(a_zip)

text = ""

for x, y in zipped_list:
    text = text + str(x) + "=" + y + "\n"

output = "C:/Temp/ablkeywords_notcomplete_komma_pr.txt"

with open(output, 'w', encoding="ANSI") as txt:
    writetext = txt.write(text)


