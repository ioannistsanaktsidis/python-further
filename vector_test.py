from math import sqrt
from pytest import mark

from vector import Vector

construction_data = ('x y'.split(),
                     ((1, 2),
                      (3, 4)))


@mark.parametrize(*construction_data)
def test_Vector_components_should_be_accessible_as_named_attributes(x, y):
    v = Vector(x, y)
    assert v.x == x
    assert v.y == y


@mark.parametrize(*construction_data)
def test_Vector_components_should_be_accessible_by_indexing(x, y):
    v = Vector(x, y)
    assert v[0] == x
    assert v[1] == y

setting_data = ('x y new_x new_y'.split(),
                ((1, 2,  3, 4),
                 (10, 20, 45, 56)))


@mark.parametrize(*setting_data)
def test_Vector_attribute_setting_should_work(x, y, new_x, new_y):
    v = Vector(x, y)
    v.x = new_x
    assert v.x == new_x
    v.y = new_y
    assert v.y == new_y


@mark.parametrize(*setting_data)
def test_Vector_setting_via_index_should_work(x, y, new_x, new_y):
    v = Vector(x, y)
    v[0] = new_x
    assert v.x == new_x
    v[1] = new_y
    assert v.y == new_y


two_vector_op_data = ('x1 y1 x2 y2'.split(),
                      ((8, 6,  2, 6),
                       (7, 4,  3, 2,)))


@mark.parametrize(*two_vector_op_data)
def test_Vector_addition_should_work(x1, y1,  x2, y2):
    u = Vector(x1, y1)
    v = Vector(x2, y2)
    w = u + v
    assert w.x == x1 + x2
    assert w.y == y1 + y2


@mark.parametrize(*two_vector_op_data)
def test_Vector_subtraction_should_work(x1, y1,  x2, y2):
    u = Vector(x1, y1)
    v = Vector(x2, y2)
    w = u - v
    assert w.x == x1 - x2
    assert w.y == y1 - y2


@mark.parametrize(*two_vector_op_data)
def test_Vector_in_place_addition_should_work(x1, y1,  x2, y2):
    u = Vector(x1, y1)
    v = Vector(x2, y2)
    u += v
    assert u.x == x1 + x2
    assert u.y == y1 + y2


@mark.parametrize(*two_vector_op_data)
def test_Vector_in_place_subtraction_should_work(x1, y1,  x2, y2):
    u = Vector(x1, y1)
    v = Vector(x2, y2)
    u -= v
    assert u.x == x1 - x2
    assert u.y == y1 - y2


@mark.parametrize(*construction_data)
def test_Vector_unary_minus_should_work(x, y):
    v = Vector(x, y)
    w = -v
    assert w.x == -x
    assert w.y == -y

vector_scalar_data = ('x y s'.split(),
                      ((1, 2, 3),
                       (8, 5, 9)))


@mark.parametrize(*vector_scalar_data)
def test_Vector_multiplication_by_scalar_on_left_should_work(x, y, s):
    v = Vector(x, y)
    w = s * v
    assert w.x == x * s
    assert w.y == y * s


@mark.parametrize(*vector_scalar_data)
def test_Vector_multiplication_by_scalar_on_right_should_work(x, y, s):
    v = Vector(x, y)
    w = v * s
    assert w.x == x * s
    assert w.y == y * s


@mark.parametrize(*vector_scalar_data)
def test_Vector_division_by_scalar_should_work(x, y, s):
    s = float(s)
    v = Vector(x, y)
    w = v / s
    assert w.x == x / s
    assert w.y == y / s


@mark.parametrize(*vector_scalar_data)
def test_Vector_in_place_multiplication_by_scalar_should_work(x, y, s):
    v = Vector(x, y)
    v *= s
    assert v.x == x * s
    assert v.y == y * s


@mark.parametrize(*vector_scalar_data)
def test_Vector_in_place_division_by_scalar_should_work(x, y, s):
    s = float(s)
    v = Vector(x, y)
    v /= s
    assert v.x == x / s
    assert v.y == y / s


@mark.parametrize(*construction_data)
def test_Vector_magnitude_should_work(x, y):
    assert abs(Vector(x, y)) == sqrt(x * x + y * y)
