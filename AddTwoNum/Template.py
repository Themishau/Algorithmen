from typing import List


def convertList(l, i):
    start = ListNode (val=int(l[i]), next=None)
    i += 1
    if i < len(l):
        start.next = convertList(l, i)
    return start

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = ListNode(val=(l1.val + l2.val), next=None)
        new = ListNode(val=0, next=None)
        if start.val > 9:
            start.val = start.val - 10
            new.val = 1
        if l1.next is None and l2.next is None:
            if new.val > 0:
                start.next = new
            return start
        elif l1.next is None:
            start.next = self.addTwoNumbers(l1=new, l2=l2.next)
        elif l2.next is None:
            start.next = self.addTwoNumbers(l1=l1.next, l2=new)
        else:
            l1.next.val = l1.next.val + new.val
            start.next = self.addTwoNumbers(l1=l1.next, l2=l2.next)
        return start


def read_node(list):
    print("run_value: {} ".format(list.val))
    if list.next is not None:
        read_node(list.next)
    return list.val


def main(input = "input.txt", output = "output.txt"):
    colours = ["red", "green", "yellow", "blue"]
    things = ["house", "car", "tree"]
    coloured_things1 = [(x + " " + y) for x in things for y in colours]
    # for x in things:
    #     for y in colours:
    #         coloured_things1 = (x + " " + y)
    coloured_things2 = [(x + " " + y) for x in colours for y in things]
    # coloured_things = [(x, y) for x in things for y in colours]
    print(coloured_things1)
    print(coloured_things2)

    result = []
    lists = []
    solution = Solution()
    with open(input, 'r', encoding="ANSI") as txt:
        for line in txt:
            print(line)
            line = line.replace('\n', '')
            line = line.split(',')
            lists.append(convertList(line, 0))
    l1 = lists[0]

    # l2 = lists[1][0]
    # read_node(l1)
    # read_node(l2)
    #
    result.append(solution.addTwoNumbers(l1=lists[0], l2=lists[1]))
    read_node(result[0])

    with open(output, 'w', encoding="ANSI") as txt:
        for line in result:
            txt.writelines(str(line) + "\n")


if __name__ == '__main__':
    main()