#pip install colored
#pip install openpyxl
from colored import fg, bg, attr
from openpyxl import *

color = fg(1) + bg(15)
print(color + "Shi" + attr(0))