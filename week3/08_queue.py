class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        # 어떻게 하면 될까요?
        #head         tail
        #[3] -> [4] -> [5]

        new_node = Node(value)
        if self.is_empty() is True:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

        return

    def dequeue(self):
        # 어떻게 하면 될까요?

        #       head    tail
        # [3] -> [4] -> [5]

        if self.is_empty():
            return  "Queue is empty"
        deleted_data = self.head.data
        self.head = self.head.next

        return  deleted_data

    def peek(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "Queue is empty"

        return  self.head.data

    def is_empty(self):
        # 어떻게 하면 될까요?
        return  self.head is None

queue = Queue()
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.is_empty())
