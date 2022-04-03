from typing import List


def convertList(l, dtype):
    return list(map(dtype, l))


class Solution:
    def Template(self, nums: List[str]) -> List[str]:
        s = {}
        print(len(nums))
        for i in nums:
            if str(i) in s:
                s[str(i)] = s[str(i)] + 1
            elif str(i) != ' ':
                s[str(i)] = 1
        s = dict(sorted(s.items(), key=lambda item: item[1],reverse=True))
        printit = ''
        for i in s:
            if list(s.values())[0] == s[i]:
                if printit == '':
                    printit = str(i)
                else:
                    printit = printit + ' ' + str(i)
        return printit

    def Template2_lists(self, nums: List[str]) -> List[str]:
        object = []
        occ    = []

        for i in nums:
            trimi = i.replace('\n', '')
            if trimi in object:
                occ[object.index(i)] = occ[object.index(i)] + 1
            elif i != ' ':
                object.append(trimi)
                occ.append(1)
        print("in liste packen: {}".format(object))
        print(occ)

        #bubble sort
        length = len(occ)
        for i in range(length - 1):
            for j in range(0, length - i - 1):
                if occ[j] < occ[j + 1]:
                    object[j], object[j + 1] = object[j + 1], object[j]
                    occ[j], occ[j + 1] = occ[j + 1], occ[j]
                elif occ[j] == occ[j + 1] and int(object[j]) > int(object[j + 1]):
                    object[j], object[j + 1] = object[j + 1], object[j]
                    occ[j], occ[j + 1] = occ[j + 1], occ[j]

        print("bubble sort: {}".format(object))
        print(occ)
        printit = ''
        # wir nehmen object und holen uns den Index, da bei occ es mehrere mit dieser Zahl geben kann
        for i in object:
            if occ[0] == occ[object.index(i)]:
                if printit == '':
                    printit = i
                else:
                    printit = printit + ' ' + i
        return printit


# input_line1 = input()
# input_line2 = input().split(' ')
#
# object = []
# occ = []
# if (int(input_line1) - 1) > 0:
#     for i in range(int(input_line1) - 1):
#         number = input_line2[i]
#         trimi = number.replace('\n', '')
#         if trimi == ' ':
#             next
#         elif trimi in object:
#             occ[object.index(trimi)] = occ[object.index(trimi)] + 1
#         elif i != ' ':
#             object.append(trimi)
#             occ.append(1)
#
#     # bubble sort
#     length = len(occ)
#     for i in range(length - 1):
#         for j in range(0, length - i - 1):
#             if occ[j] < occ[j + 1]:
#                 object[j], object[j + 1] = object[j + 1], object[j]
#                 occ[j], occ[j + 1] = occ[j + 1], occ[j]
#             elif occ[j] == occ[j + 1] and int(object[j]) > int(object[j + 1]):
#                 object[j], object[j + 1] = object[j + 1], object[j]
#                 occ[j], occ[j + 1] = occ[j + 1], occ[j]
#
#     printit = ''
#     # wir nehmen object und holen uns den Index, da bei occ es mehrere mit dieser Zahl geben kann
#     for i in object:
#         if occ[0] == occ[object.index(i)]:
#             if printit == '':
#                 printit = i
#             else:
#                 printit = printit + ' ' + i
#     print(printit)
# else:
#     print('')


def main(input = "input.txt", output = "output.txt"):
    result = []
    solution = Solution()
    with open(input, 'r', encoding="ANSI") as txt:
        for line in txt:
            line = line.split(' ')
            line = convertList(line, str)
            result.append(solution.Template2_lists(nums=line))

    with open(output, 'w', encoding="ANSI") as txt:
        for line in result:
            print(line)
            txt.writelines(str(line) + "\n")


if __name__ == '__main__':
    main()