from pydantic.types import PositiveInt


class MaxHeap:

    def __init__(self):
        self.heap_list = [None]
        self.length = 0

    def add_value(self, value: int):
        self.length += 1
        self.heap_list += [value]
        if self.length > 1:
            self._heapify_up()

    def _heapify_up(self):
        if self.length > 1:
            for i in range(self.length, 1, -1):
                parent_idx = self.get_parent_idx(idx=i)
                if self.heap_list[parent_idx] < self.heap_list[i]:
                    self._swap_heap_list_elements(i, parent_idx)

    def _swap_heap_list_elements(self, i, j):
        self.heap_list[i], self.heap_list[j] = self.heap_list[j], self.heap_list[i]

    @staticmethod
    def get_parent_idx(idx: PositiveInt) -> PositiveInt:
        return idx // 2

    @staticmethod
    def get_left_child_idx(idx: PositiveInt) -> PositiveInt:
        return idx*2

    @staticmethod
    def get_right_child_idx(idx: PositiveInt) -> PositiveInt:
        return idx*2 + 1

    def __str__(self):
        if self.length > 0:
            return " --> ".join([ "[" + str(el) + "]" for el in self.heap_list[1:]])
        else:
            return "[]"


if __name__ == "__main__":
    max_heap = MaxHeap()
    print(max_heap)

    max_heap.add_value(21)
    print(max_heap)

    max_heap.add_value(30)
    print(max_heap)

    max_heap.add_value(40)
    print(max_heap)
