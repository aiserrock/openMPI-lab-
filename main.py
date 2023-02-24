import numpy as np
import matplotlib.pyplot as plt

# threads number
THREADS = 6
# number of seconds and number of threads
SEC_LIST = [35, 17.2, 11.1, 9.72, 9.43, 9]
# thread named alias
NAMED_THREADS = ['One', 'Two', 'Three', 'Four', 'Five', 'Six']


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
