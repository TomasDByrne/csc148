"""CSC148 Lab 5: Linked Lists

=== CSC148 Winter 2024 ===
Department of Computer Science,
University of Toronto

=== Module description ===

This module runs timing experiments to determine how the time taken
to call `len` on a Python list vs. a LinkedList grows as the list size grows.
"""
from timeit import timeit
from linked_list import LinkedList
from typing import Callable

SIZES = [1000, 2000, 4000, 8000, 16000]  # The list sizes to try.
NUM_TRIALS = 20                          # The number of trials to run.


def _setup_lists(lsize: int, n: int, list_type: Callable) -> list[LinkedList]:
    """Return a list of <n> <list_type> objects, each with <lsize> elements.

    Preconditions:
    - list_type is a class (e.g. list or LinkedList)
    - list_type has the __len__ method implemented
    - list_type can be constructed by passing in a list of elements
      e.g. list([1, 2, 3]) creates a list with items [1, 2, 3]
           LinkedList([1, 2, 3]) creates a LinkedList with items
           [1, 2, 3] as well.

    >>> lnks = _setup_lists(1, 2, LinkedList)
    >>> len(lnks)
    2
    >>> len(lnks[0])
    1
    >>> len(lnks[1])
    1
    >>> isinstance(lnks[0], LinkedList)
    True
    >>> lsts = _setup_lists(1, 2, list)
    >>> len(lsts)
    2
    >>> len(lsts[0])
    1
    >>> len(lsts[1])
    1
    >>> isinstance(lsts[0], list)
    True
    """
    # TODO: Implement this helper function.
    hold = []
    item = []
    for i in range(lsize):
        item.append(1)
    for j in range(n):
        item.append(list_type(item))
    return item


def time_len(list_type: Callable) -> list[float]:
    """Run timing experiments for len on lists of type list_type, returning a
    list of times with the average time it took to run len on list_type objects
    with sizes SIZES over NUM_TRIALS trials.

    Preconditions:
    - (list_type is list) or (list_type is LinkedList)
    """
    times = []

    # We have given you the code for testing len on Python's built-in list below,
    # based on the code from Lab 4.
    for size in SIZES:
        time = 0
        lists = _setup_lists(size, NUM_TRIALS, list_type)
        for lst in lists:
            time += timeit('len(lst)', number=1, globals=locals())

        average_time = time / NUM_TRIALS * 1e6
        times.append(average_time)
        print(f'len: List size {size:>7}, time: {average_time}')

    return times



def plot_experiment() -> None:
    """Run the timing experiment on AddToStartQueue and AddToEndQueue
     and plot a graph."""
    import matplotlib.pyplot as plt

    # Run the experiments and store the results
    linktimes, ltime = time_len(LinkedList), time_len(list)

    # Plot the results of our experiments and assign labels to each plot.
    # Our call to plt.plot takes 3 arguments:
    #     - The x-coordinates of the values to plot
    #     - The y-coordinates of the values to plot
    #     - The format we want to plot with.
    #       'ro' is 'red circle'
    #       'bo' is 'blue circle'
    #       Other formats include 'rx' (red X), 'bx' (blue X) and many more!
    start_plt, = plt.plot(SIZES, linktimes, 'ro')
    start_plt.set_label("LinkedList.enqueue")

    end_plt, = plt.plot(SIZES, ltime, 'bo')
    end_plt.set_label("BuiltinList.enqueue")

    # After we finish plotting everything, we can create the legend of
    # our graph and label the axes
    plt.legend()
    plt.xlabel("Queue Size")
    plt.ylabel("Average Time (μs)")

    # Show our plotted results. This line must be called after
    # all of the other setup.
    plt.show()


if __name__ == '__main__':
    print("Running len(lst) experiments...")
    time_len(list)

    print("Running len(LinkedList) experiments...")
    time_len(LinkedList)

    print("plotting")
    plot_experiment
    # TODO: After you implement a function to run the timing experiment,
    #       Add a call to that function below.
