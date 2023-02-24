import numpy as np
import matplotlib.pyplot as plt

# threads number
THREADS = 4
# number of seconds and number of threads
SEC_LIST = [70, 35.2, 21.1, 18.72]
# thread named alias
NAMED_THREADS = ['One', 'Two', 'Three', 'Four',]


def get_graph():
    x_list = list(range(0, THREADS))
    x_indexes = np.arange(len(x_list))
    plt.title('threads runtime')
    plt.xlabel('threads')
    plt.ylabel('sec')
    plt.xticks(x_indexes, NAMED_THREADS)
    plt.plot(x_list, SEC_LIST, label="runtime", marker='o')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    get_graph()
