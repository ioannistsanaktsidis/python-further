from pytest import mark


class Window(object):
    """docstring for Window"""

    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height

    @staticmethod
    def fromCorners(corner1, corner2):
        width = corner2[0] - corner1[0]
        height = corner2[1] - corner1[1]
        c = Window(corner1, width, height)
        return c

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (2 * self.width) + (2 * self.height)
# Tests start here


class BorderWindow(Window):
    """docstring for Window"""

    def __init__(self, corner, width, height):
        super(BorderWindow, self).__init__(corner, width, height)


window_data = ("corner width height".split(),
               ((1, 2, 3),
                (2, 4, 5)))


@mark.parametrize(*window_data)
def test_class_is_contructable(corner, width, height):
    c = Window(corner, width, height)
    assert c.corner == corner
    assert c.width == width
    assert c.height == height


@mark.parametrize(*window_data)
def test_class_has_area_method(corner, width, height):
    c = Window(corner, width, height)
    assert c.area() == width * height


@mark.parametrize(*window_data)
def test_class_has_perimeter_method(corner, width, height):
    c = Window(corner, width, height)
    assert c.perimeter() == (2 * width) + (2 * height)


corner_data = ("corner1 corner2  width height".split(),
               (((1, 2),
                 (3, 4), 2, 2), ((5, 10),
                                 (10, 20), 5, 10)))


@mark.parametrize(*corner_data)
def test_class_is_contructable_by_coordinates(corner1, corner2, width, height):
    c = Window.fromCorners(corner1, corner2)
    assert c.width == width
    assert c.height == height
