from time import sleep
from operator import itemgetter
from queue import Queue

INF = float("inf")

example_cells = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331],
]


def get_neighbors(row, col, n_rows, n_cols):
    if row > 0:
        yield row - 1, col
    if col > 0:
        yield row, col - 1
    if row < n_rows - 1:
        yield row + 1, col
    if col < n_cols - 1:
        yield row, col + 1


def cyan_bold(s):
    return f"\033[1;36m{s}\033[0m"


def show_grid(queue, n_rows, n_cols):
    """
    e.g.
    to_process = show_grid(to_process, n_rows, n_cols)
    """
    highlight = set()
    temp = Queue()
    while not queue.empty():
        obj = queue.get()
        highlight.add(obj[1])
        temp.put(obj)

    for row in range(n_rows):
        for col in range(n_cols):
            if (row, col) in highlight:
                c = cyan_bold("*")
            else:
                c = "*"
            print(c, end="")
        print()
    print("---")

    return temp


def main(cells):
    n_rows, n_cols = len(cells), len(cells[0])
    initial_cells = [(i, 0) for i in range(n_rows)]
    min_vals = get_minimal_values(cells, initial_cells, n_rows, n_cols)
    return min(map(itemgetter(-1), min_vals))


def get_minimal_values(cells, initial_cells, n_rows, n_cols, verbose=0):
    grid = [[INF] * n_cols for _ in range(n_rows)]
    to_process = Queue()
    for row, col in initial_cells:
        to_process.put((cells[row][col], (row, col)))

    while not to_process.empty():
        val, (row, col) = to_process.get()
        if val < grid[row][col]:
            grid[row][col] = val
            for orow, ocol in get_neighbors(row, col, n_rows, n_cols):
                oval = cells[orow][ocol]
                to_process.put((val + oval, (orow, ocol)))

        if verbose > 0:
            to_process = show_grid(to_process, n_rows, n_cols)
            sleep(0.1)

    return grid


if __name__ == "__main__":
    assert main(example_cells) == 994

    cells = []
    for line in open("input/0082_matrix.txt").read().strip().split():
        cells.append(list(map(int, line.split(","))))
    assert main(cells) == 260324
    print("done")
