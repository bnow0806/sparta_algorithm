class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break



#1. 루트 노드와 끝 노드를 교체한다.
#2. 맨 뒤의 원소를 삭제한다.
#3. 변경된 노드를 더 큰 자식 노드와 비교, 반복
#4. 가장 아래 도달 시 멈춤

    def delete(self):
        # 구현해보세요!
        cur_index=len(self.items)-1

        self.items[1],self.items[cur_index] = self.items[cur_index], self.items[1]

        deleted_value = self.items[cur_index]
        self.items.remove(deleted_value)
        #print(self.items)

        cur_index = 1
        while cur_index<len(self.items):
            # if cur_index*2+1 <= len(self.items)-1:  #오른쪽 자식 노드
            #     child_index = cur_index*2+1
            # else:                                   #왼쪽 자식 노드
            #     child_index = cur_index*2
            #
            # if child_index > len(self.items)-1:     #마지막 도달 시 탈출
            #     break
            #
            # if self.items[cur_index] <= self.items[child_index]:
            #     self.items[cur_index],self.items[child_index] = self.items[child_index],self.items[cur_index]
            #     cur_index=child_index

            max_index =cur_index
            left_child_index =cur_index*2
            right_child_index = cur_index*2+1
            # 둘 중 큰 값
            #왼쪽 자식 노드
            if left_child_index< len(self.items)-1 and self.items[max_index] <= self.items[left_child_index]:
                max_index = left_child_index

            #오른쪽 자식 노드
            if right_child_index < len(self.items)-1 and self.items[max_index] <= self.items[right_child_index]:
                max_index = right_child_index

            self.items[max_index], self.items[cur_index] = self.items[cur_index], self.items[max_index]
            cur_index = max_index

            if max_index == cur_index:  #조건을 만족하지 않아 위에 if를 실행 안할 때
                break


        print(self.items)

        return   deleted_value# 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
#print(max_heap.items)  # [None, 7, 6, 4, 2, 5]