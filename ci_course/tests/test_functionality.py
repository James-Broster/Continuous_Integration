import ci_course


def test_greet():
    """
    Test the function `greet` in functionality.py
    """
    assert ci_course.greet() == "Hello "
    assert ci_course.greet("Fergus") == "Hello Fergus"
    assert ci_course.greet(5) is None


def test_minimum():
    """
    Test the function `minimum` in functionality.py
    """
    assert ci_course.minimum(1, 2, 3) == 1
    assert ci_course.minimum(1.2, 2.3) == 1.2
    assert ci_course.minimum(-1.2, -3) == -3
    assert ci_course.minimum("hello", "goodbye") is None
