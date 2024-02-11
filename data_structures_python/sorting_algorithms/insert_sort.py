import numpy as np


def insert_sort(list_: list[int]):
    for i in range(1, len(list_)):
        for j in range(i, 0, -1):
            if list_[j-1] > list_[j]:
                list_[j-1], list_[j] = list_[j], list_[j-1]
            else:
                break
    return list_


if __name__ == "__main__":
    my_list = list(np.random.randint(1, 1001, 100))
    print(insert_sort(list_=my_list))
