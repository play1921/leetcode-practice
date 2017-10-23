# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
                :type l1: ListNode
                :type l2: ListNode
                :rtype: ListNode
                """
        num_one = 0
        num_two = 0
        count_one = 0
        count_two = 0
        while l1 is not None:
            num_one += l1.val * 10 ** count_one
            l1 = l1.next
            count_one += 1

        while l2 is not None:
            num_two += l2.val * 10 ** count_two
            l2 = l2.next
            count_two += 1

        sum_l1_l2 = num_one + num_two
        head_node = ListNode(sum_l1_l2 % 10)
        current_node = head_node
        sum_l1_l2 //= 10

        while sum_l1_l2 / 10 > 0:
            new_node = ListNode(sum_l1_l2 % 10)
            current_node.next = new_node
            current_node = new_node
            sum_l1_l2 //= 10

        return head_node


if __name__ == '__main__':
    l1_node_first = ListNode(2)
    l1_node_second = ListNode(4)
    l1_node_third = ListNode(3)
    l1_node_first.next = l1_node_second
    l1_node_second.next = l1_node_third

    l2_node_first = ListNode(5)
    l2_node_second = ListNode(6)
    l2_node_third = ListNode(4)
    l2_node_first.next = l2_node_second
    l2_node_second.next = l2_node_third

    print("ListNode 1: {} -> {} -> {}".format(l1_node_first.val, l1_node_second.val, l1_node_third.val))
    print("ListNode 2: {} -> {} -> {}".format(l2_node_first.val, l2_node_second.val, l2_node_third.val))
    print("Should be: 7 -> 0 -> 8")

    solution = Solution()
    answer = solution.addTwoNumbers(l1_node_first, l2_node_first)
    answer_list = [answer.val]

    while answer.next is not None:
        answer = answer.next
        answer_list.append(answer.val)

    print('Answer is: ' + ' -> '.join(str(i) for i in answer_list))
