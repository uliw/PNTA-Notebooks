from typing import Any

d = {
    "Brian": 0,
    "Bob": [1, 2, 3, 4, 5, 6, 7, 8],
    "Sam": {"Exams": 75, "Other": 90},
    "Liam": [1, 2],
}


def fl(l: list | tuple) -> str:
    """return the first 3 and the last element of a list
    e.g., [1, 2, 3, .... 7]
    """
    s = "["
    for e in l[:3]:
        s = f"{s}{fv(e,0)}, "
    s = f"{s}..., {fv(l[-1],0)}]"

    return s


def fv(v: Any, level) -> str:
    """return a fomatted string of v

    for numbers return the number according to
    country setting.

    for strings, return the string.

    For list and tupels, return the first 3 elements and the last
    e.g., [1, 2, 3, ... 7]

    raise and error for everything else
    """
    s = ""
    if isinstance(v, str):
        s = f"{v}"
    elif isinstance(v, (int, float)):
        s = f"{v:n}"
    elif isinstance(v, (list, tuple)):
        s = fl(v)
    elif isinstance(v, (dict)):
        level = level + 1
        s = f"{fd(v, level)}"
    else:
        raise ValueError(f"no definition for {type(v)}")

    return s


def fd(d: dict, level=0) -> str:
    """Format a dictionary, so that it can be printed nicely
    d = {
    "Brian": 0,
    "Bob": [1, 2, 3, 4, 5, 6, 7, 8],
    "Sam": {"Exams": 75, "Quizzes": 90},
    "Liam": [1, 2],
    }
    should print as

    Brian:	0
    Bob:	[1, 2, 3, ..., 8]
    Sam:	Exams:	 75
                Quizzes: 90

    Liam:	[1, 2]

    """

    i = 0
    s = ""
    for key, value in d.items():
        if level > 0 and i > 0:
            ind = "\t" * level
        else:
            ind = "\t" * (level - 1)

        line = f"{ind}{key}:\t{fv(value, level)}\n"
        s = s + line
        i = i + 1
    return s


# print(fd(d))

k: list[Any] = [
    1.000012,
    2e13,
    [
        1,
        2,
        3,
        4,
        5,
        6,
        78,
        [*"Hello World"],
    ],
]
print(fl(k))
