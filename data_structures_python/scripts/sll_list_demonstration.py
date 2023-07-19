import logging
from data_structures_python.lists.sll_list import SllList

logger = logging.getLogger(name=__name__)


if __name__ == "__main__":
    dict_ = {
        "a": 32,
        "b": 111,
        "c": 901
    }

    list_ = [el for el in dict_.items()]

    print("Done")