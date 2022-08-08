# pytitler

Python package that allows you to easily make pretty title for your python program

Developed by Flowseal (c) 2022

## How To Use

Installing
```
pip3 install pytitler
```

One string title
```python
from pytitler import pytitler
from pytitler.pytitler import TitleFill, TitleColors

banner = pytitler.align_titles("My first calculator!", center_x=True, center_y=True)
pytitler.print_title(banner, (TitleColors.BLURPLE, (255, 255, 255)), TitleFill.HORIZONTAL)
```

ASCII Example

```python
from pytitler import pytitler
from pytitler.pytitler import TitleFill, TitleColors

ascii1 = r'''
████████▄     ▄████████   ▄▄▄▄███▄▄▄▄    ▄██████▄  ███▄▄▄▄             
███   ▀███   ███    ███ ▄██▀▀▀███▀▀▀██▄ ███    ███ ███▀▀▀██▄           
███    ███   ███    █▀  ███   ███   ███ ███    ███ ███   ███           
███    ███  ▄███▄▄▄     ███   ███   ███ ███    ███ ███   ███           
███    ███ ▀▀███▀▀▀     ███   ███   ███ ███    ███ ███   ███           
███    ███   ███    █▄  ███   ███   ███ ███    ███ ███   ███           
███   ▄███   ███    ███ ███   ███   ███ ███    ███ ███   ███           
████████▀    ██████████  ▀█   ███   █▀   ▀██████▀   ▀█   █▀            
                                                                       '''



ascii12 = r"""
       █████████████████████
    ████▀                 ▀████
  ███▀                       ▀███
 ██▀                           ▀██
█▀                               ▀█
█                                 █
█   █████                 █████   █
█  ██▀▀▀███             ███▀▀▀██  █
█  ██▀▀▀▀▀██           ██▀▀▀▀▀██  █
█  ██▀▀▀▀▀▀██         ██▀▀▀▀▀▀██  █
█▄  ████▀▀▀▀██       ██▀▀▀▀████  ▄█
▀█▄   ▀███▀▀▀██     ██▀▀▀███▀   ▄█▀
  █▄    ▀█████▀     ▀█████▀    ▄█
  ██           ▄█ █▄           ██
  ██           ██ ██           ██
  ██                           ██
  ▀██  ██▀██  █  █  █  ██▀██  ██▀
   ▀████▀ ██  █  █  █  ██ ▀████▀
          ██  █  █  █  ██  
          ██  █  █  █  ██
          ██  █  █  █  ██
           █▄▄█▄▄█▄▄█▄▄█"""

banner = pytitler.join_titles((ascii1, ascii12), center=True)
banner = pytitler.align_titles(banner, center_x=True, center_y=True)
pytitler.print_title(banner, (TitleColors.BLURPLE, (255, 255, 255)), TitleFill.DIAGONAL_BACKWARDS)
```

## Result
![](./images/calc.png)

![](./images/demon.png)

## Gradient types
**Static**: color a text with a static color

**Vertical**: fade a text vertically

**Horizontal**: fade a text horizontally

**Diagonal**: fade a text diagonally

**DiagonalBackwards**: fade a text diagonally but backwards
