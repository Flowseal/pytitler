import functools
from enum import Enum
from pystyle import *


class ColorTypeError(Exception):
    pass


class TitleColors(Enum):
    TEAL = (26, 188, 156)
    DARK_TEAL = (17, 128, 106)
    GREEN = (46, 204, 113)
    DARK_GREEN = (31, 139, 76)
    BLUE = (52, 152, 219)
    DARK_BLUE = (32, 102, 148)
    PURPLE = (155, 89, 182)
    DARK_PURPLE = (113, 54, 138)
    MAGENTA = (233, 30, 99)
    DARK_MAGENTA = (173, 20, 87)
    GOLD = (241, 196, 15)
    DARK_GOLD = (194, 124, 14)
    ORANGE = (230, 126, 34)
    DARK_ORANGE = (168, 67, 0)
    RED = (231, 76, 60)
    DARK_RED = (153, 45, 34)
    LIGHTER_GREY = (149, 165, 166)
    DARK_GREY = (96, 125, 139)
    LIGHT_GREY = (151, 156, 159)
    DARKER_GREY = (84, 110, 122)
    BLURPLE = (114, 137, 218)
    GREYPLE = (153, 170, 181)


class TitleFill(Enum):
    STATIC = 0
    VERTICAL = 1
    HORIZONTAL = 2
    DIAGONAL = 3
    DIAGONAL_BACKWARDS = 4


def join_titles(titles: tuple, center: bool = False, spaces: int = 0) -> str:
    """
    Joining a list of strings with custom space between and centering
    """
    return functools.reduce(lambda t1, t2: Add.Add(t1, t2, center=center, spaces=spaces), titles)


def align_titles(title: str, center_x: bool = False, center_y: bool = False) -> str:
    """
    Aligning a string with X/Y of current terminal screen
    """
    if not center_x and not center_x:
        return title
    if center_x and center_y:
        return Center.Center(title)
    if center_x:
        return Center.XCenter(title)
    if center_y:
        return Center.YCenter(title)


def print_title(title: str, color: tuple | TitleColors, fill: TitleFill):
    """
    title: str
        Title to color-print
    color: tuple | tuple
        Use single color if you are filling TitleFill.STATIC, otherwise use a tuple of colors
        Raises ColorTypeError on except
    fill: TitleFill
        Static                   |           color a text with a static color
        Vertical                 |           fade a text vertically
        Horizontal               |           fade a text horizontally
        Diagonal                 |           fade a text diagonally
        DiagonalBackwards        |           fade a text diagonally but backwards
    """
    def make_col(c: tuple) -> str:
        return f"\033[38;2;{c[0]};{c[1]};{c[2]}m"

    if isinstance(color, TitleColors):
        color = color.value
    if not isinstance(color[0], int) and fill == TitleFill.STATIC:
        raise ColorTypeError("Attempt to use few colors with a static filling")
    if isinstance(color[0], int) and fill != TitleFill.STATIC:
        fill = TitleFill.STATIC

    col = list()
    if isinstance(color[0], int):
        col.append(make_col(color))
    else:
        for c in color:
            if isinstance(c, TitleColors):
                col.append(make_col(c.value))
            else:
                col.append(make_col(c))

    match fill:
        case TitleFill.STATIC:
            return print(Colorate.Color(col[0], title))
        case TitleFill.VERTICAL:
            return print(Colorate.Vertical(Col.DynamicMIX(col), title))
        case TitleFill.HORIZONTAL:
            return print(Colorate.Horizontal(Col.DynamicMIX(col), title))
        case TitleFill.DIAGONAL:
            return print(Colorate.Diagonal(Col.DynamicMIX(col), title))
        case TitleFill.DIAGONAL_BACKWARDS:
            return print(Colorate.DiagonalBackwards(Col.DynamicMIX(col), title))
