class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        # 어떻게 하면 될까요?
        # head
        # [3] -> [4]

        new_node=Node(value)
        new_node.next = self.head
        self.head = new_node

        return  new_node.data

    # pop 기능 구현
    def pop(self):
        # 어떻게 하면 될까요?

        #        head
        # [3] -> [4]

        deleted_data = self.head.data
        self.head=self.head.next

        return  deleted_data

    def peek(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "stack is none"
        return  self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        # 어떻게 하면 될까요?
        return self.head is None

#scenario

stack = Stack()
stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.is_empty())
print(stack.pop())
print(stack.is_empty())

