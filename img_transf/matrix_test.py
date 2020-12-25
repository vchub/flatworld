# создает matrix из нулей заданной ширины и высоты
def zero_matrix(width, height) -> list:
    """creates matrix of zeroes, of given width and height"""
    return [[0 for _ in range(width)] for _ in range(height)]


def test_zero():
    assert zero_matrix(1, 1) == [[0]]
    assert zero_matrix(2, 3) == [
        [0, 0],
        [0, 0],
        [0, 0],
    ]

    # check assignment
    a = zero_matrix(3, 3)
    a[0][0] = 1
    assert a[0][0] == 1
    assert a[1][0] != 1
    assert a[0][1] != 1


# делает копию matrix заданной ширины и высоты
def copy(a: list, width: int, height: int) -> list:
    b = zero_matrix(width, height)
    NotImplemented


def test_copy():
    a = zero_matrix(2, 3)
    a[0][0] = 1
    b = copy(a, width=2, height=3)
    b[1][0] = 2
    assert a[0][0] == 1
    assert b[0][0] == 1
    assert b[1][0] == 2
    assert a[1][0] == 0


# увеличивает matrix заданной ширины и высоты в factor раз
def scale(a: list, width: int, height: int, factor: int) -> list:
    b = zero_matrix(width * factor, height * factor)
    NotImplemented


def xtest_scale():
    a = [[1]]
    b = scale(a, 1, 1, 1)
    assert b == [[1]]

    b = scale(a, 1, 1, 3)
    assert b == [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]

    a = [[1, 2, 3], [4, 5, 6]]
    b = scale(a, 3, 2, 3)
    # print(b)
    assert len(b) == 2 * 3
    assert len(b[0]) == 3 * 3
    assert b[1 * 3][2 * 3] == 6
