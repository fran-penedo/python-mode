"""One liner.

Multi line.

Docstring.

"""

import math


def top_function(a, b, c):
    """One liner docstring.

    """
    print(a)
    print(b)
    print(c)


def foo(
    asdfasdfasdfasdf,
    afdsfsdfasdfasfdf,
    afdsfadsfasdfa,
    asdfdfdsafsdasdf,
    asdfdfddsasfasdf,
):
    x = 5
    return x


def foo(
    asdfasdfasdfasdf,
    afdsfsdfasdfasfdf,
    afdsfadsfasdfa,
    asdfdfdsafsdasdf,
    asdfdfddsasfasdf,
) -> Iterable[T]:
    x = 5
    return x


class Foo:
    """foo

    """

    def foo(
        asdfasdfasdfasdf,
        afdsfsdfasdfasfdf,
        afdsfadsfasdfa,
        asdfdfdsafsdasdf,
        asdfdfddsasfasdf,
    ) -> Iterable[T]:
        pass


def bar():
    """Foobar

    """
    if (
        asdfasdfasdfasdfasdfasdf == 0
        and dafsdfasdfasdfasdfasdf == 3
        and asfadsfasdfasdfasdfa == 2
    ):
        pass

    def _bar():
        pass

    return _bar


if __name__ == "__main__":
    top_function(math.e, 1, "si")
