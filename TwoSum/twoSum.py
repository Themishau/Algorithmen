from typing import List
import sys
import argparse

def convertList(l, dtype):
    return list(map(dtype, l))

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # number : index
        index_seen = {}
        for i, num in enumerate(nums, start=0): # i =  index, num = value
            """
            careful with dicts!
            >>> "in" in {"in": "out"}
            True
            >>> "in" in {"out": "in"}
            False
            """
            if target - num in index_seen:
                return[index_seen[target - num], i] # returns index of the two digits
            # saves the number als key and index as value
            elif num not in index_seen:
                index_seen[num] = i
                try: #look ahead
                    if target - nums[i + 1] in index_seen:
                        return [index_seen[target - nums[i + 1]], i+1]
                except KeyError:
                    pass


def main(input = "input.txt", output = "output.txt"):

    parser = argparse.ArgumentParser(description='Alg')
    parser.add_argument('inputfile', help='input.txt')
    parser.add_argument('outputfile', help='output.txt')

    args = parser.parse_args()

    result = []
    input_data = []
    target = []
    solution = Solution()

    i = 0
    j = 0
    with open(args.inputfile, 'r') as txt:
        for line in txt:
            if i % 2:
                print(line)
                line = line.split(',')
                line = convertList(line, int)
                target.append(line)
            else:
                print(line)
                line = line.split(',')
                line = convertList(line, int)
                input_data.append(line)
            i += 1

    for i in range(0, len(target)):
        for j in range(0, len(target[i])):
            result.append(solution.twoSum(nums=input_data[i], target=target[i][j]))

    with open(args.outputfile, 'w', encoding="ANSI") as txt:
        for line in result:
            print(line)
            txt.writelines(str(line) + "\n")


if __name__ == '__main__':
    main()