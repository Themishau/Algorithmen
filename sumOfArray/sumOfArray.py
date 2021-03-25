from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if len(result) != 0:
                result.append(num + result[-1])
            else:
                result.append(num)
        return result


def convertList(l, dtype):
    return list(map(dtype, l))

def main(input = "input.txt", output = "output.txt"):
    result = []
    solution = Solution()
    with open(input, 'r', encoding="ANSI") as txt:
        for line in txt:
            print(line)
            line = line.split(',')
            line = convertList(line, int)
            result.append(solution.runningSum(nums=line))

    with open(output, 'w', encoding="ANSI") as txt:
        for line in result:
            print(line)
            txt.writelines(str(line) + "\n")



if __name__ == '__main__':
    main()