class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        # 구현해보세요!

        #뒤에서 k 번째 -> 앞에서 n-k+1번째
        #5에서 2번째 -> 앞에서 (5-2)+1=4번째
        cur = self.head
        length =0

        while cur is not None:
            length += 1
            cur = cur.next

        print("length",length)

        end_length = length - k

        cur = self.head
        for n in range(end_length):  # end_length 번째
            cur = cur.next

        return cur



linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
#print(linked_list.get_kth_node_from_first(3).data)


#개선
# def get_kth_node_from_last(self, k):
#     slow = self.head
#     fast = self.head
#
#     for i in range(k):
#         fast = fast.next
#
#     while fast is not None:
#         slow = slow.next
#         fast = fast.next
#
#     return slow