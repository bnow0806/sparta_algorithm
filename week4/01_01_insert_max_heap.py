#1. 맨 마지막에 원소 넣기
#2. 부모 노드와 비교, 크다면 자리 변경 / 반복
#3. 도달 시 멈춤

class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        # 구현해보세요!
        self.items.append(value)

        # 처음 시도
        n=len(self.items)
        child_node_index = n-1
        parent_node_index = (n-1)//2

        #print("child_node_index",child_node_index,"parent_node_index",parent_node_index)
        #if self.items[parent_node_index] !=None:

        while (self.items[parent_node_index] !=None) and (self.items[parent_node_index] <= self.items[child_node_index]):
            self.items[parent_node_index], self.items[child_node_index] = self.items[child_node_index], self.items[parent_node_index]

            child_node_index = parent_node_index    #node 순서 바꿨으니까 대입
            parent_node_index = child_node_index//2 #새로운 parent node 비교대상
            #print(self.items)

        return  self.items


max_heap = MaxHeap()
max_heap.insert(3)
print(max_heap.items)
max_heap.insert(4)
print(max_heap.items)
max_heap.insert(2)
print(max_heap.items)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!