def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    shape_ = [[0 for n in range(shape[1]+2)] for m in range(0, shape[0]+2)]
    shape_[0][0] = 1
    for i in range(0, len(shape_)-2):
        for j in range(0, len(shape_[i])-2):
            shape_[i][j] += shape_[i - 1][j - 2] * 2 + shape_[i - 2][j - 1] * 2 + shape_[i - 1][j + 2] * 2 + shape_[i - 2][j + 1] * 2
    return shape_[point[0]][point[1]]


if __name__ == '__main__':
    print(calculate_paths((8, 8), (7, 7)))
    print(calculate_paths((9, 9), (8, 8)))
    print(calculate_paths((17, 12), (16, 9)))
    print(calculate_paths((12, 10), (11, 9)))
