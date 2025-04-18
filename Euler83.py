from Euler82 import get_minimal_values, example_cells


def main(cells):
    n_rows, n_cols = len(cells), len(cells[0])
    initial_cells = [(0, 0)]
    min_vals = get_minimal_values(cells, initial_cells, n_rows, n_cols, verbose=0)
    return min_vals[-1][-1]


assert main(example_cells) == 2297
cells = []
for line in open("input/0082_matrix.txt").read().strip().split():
    cells.append(list(map(int, line.split(","))))
print(main(cells))
print("done")
