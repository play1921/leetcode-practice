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
        carry = 0
        dummy_head_node = ListNode(0)
        currnet_node = dummy_head_node

        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            sum_x_y = x + y + carry
            carry = (x + y + carry) // 10
            currnet_node.next = ListNode(sum_x_y % 10)
            currnet_node = currnet_node.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        if carry > 0:
            currnet_node.next = ListNode(carry)

        return dummy_head_node.next


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
