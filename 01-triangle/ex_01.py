def triangle_hyp(a, b):
    """Calculates the hypothenusis of a right triangle.

    Args:
        a (float): one cathetus
        b (float): one cathetus

    Returns:
        float: the hypothenusis
    """
    c = pow(pow(a, 2)+pow(b, 2), 0.5)
    return c


def triangle_area(a, b):
    """Calculates the area of a right triangle.

    Args:
        a (float): one cathetus
        b (float): one cathetus

    Returns:
        float: the area
    """
    return (a*b) / 2


def triangle_circ(a, b):
    """Calculates the circumference of a right triangle.

    Args:
        a (float): one cathetus
        b (float): one cathetus

    Returns:
        float: the circumference
    """
    return a + b + triangle_hyp(a, b)


if __name__ == "__main__":
    a = float(input("a: "))
    b = float(input("b: "))
    c = triangle_hyp(a, b)
    print('c: %.3f' % c)
    A = triangle_area(a, b)
    print('A: %.3f' % A)
    C = triangle_circ(a, b)
    print('C: %.3f' % C)
