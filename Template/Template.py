from typing import List


def convertList(l, dtype):
    return list(map(dtype, l))


class Solution:
    def Template(self, nums: List[int]) -> List[int]:
        return nums

def main(input = "input.txt", output = "output.txt"):
    result = []
    solution = Solution()
    with open(input, 'r', encoding="ANSI") as txt:
        for line in txt:
            print(line)
            line = line.split(',')
            line = convertList(line, int)
            result.append(solution.Template(nums=line))


    with open(output, 'w', encoding="ANSI") as txt:
        for line in result:
            print(line)
            txt.writelines(str(line) + "\n")


if __name__ == '__main__':
    main()