
import sys
import os
import platform
import importlib

# define folder path
DIR_PYSCRIPT = os.path.abspath(os.path.join(__file__, "../"))
DIR_SOURCE   = os.path.abspath(os.path.join(__file__, "../../"))
DIR_PROJECT  = os.path.abspath(os.path.join(__file__, "../../../"))
# DIR_DATA     = os.path.abspath(os.path.join(DIR_PROJECT, "./data/"))
# DIR_FIG      = os.path.abspath(os.path.join(DIR_PROJECT, "./fig/"))
DIR_TEST     = os.path.abspath(os.path.join(DIR_PROJECT, "./source/_test/"))

# os info
OsName    = platform.system()
OsVersion = platform.version()
OsInfo    = platform.platform()
OsRelease    = platform.release()
OsArchitecture = platform.architecture()

# define plotting colors
COLOR_BLUE   = "#05A6F0"
COLOR_RED    = "#F35325"
COLOR_GREEN  = "#81BC06"
COLOR_YELLOW = "#FFBA08"
COLOR_PURPLE = "#986DBF"

COLOR_LIST = [
    COLOR_BLUE,
    COLOR_RED,
    COLOR_GREEN,
    COLOR_YELLOW,
    COLOR_PURPLE,
]

COLOR_MAP = {
    "blue": COLOR_BLUE,
    "red": COLOR_RED,
    "green": COLOR_GREEN,
    "yellow": COLOR_YELLOW,
    "purple": COLOR_PURPLE,
}

# define color of terminal
class TermColor():
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET     = '\033[0m'

CMSG_YES = TermColor.GREEN + "YSE" + TermColor.RESET
CMSG_NO  = TermColor.RED   + "NO" + TermColor.RESET

# pip package 
def check_pip_package(name):
    spec = importlib.util.find_spec(name)
    if spec is not None:
        print("%-15s %-5s" % (name, CMSG_YES))
        return True
    else:
        print("%-15s %-5s" % (name, CMSG_NO))
        return False

def mkdir(abspath):
        if not os.path.isdir(abspath):
            os.mkdir(abspath)

def print_bar(name):
    print(TermColor.BLUE + '===== {:^10s} ====='.format(name)+ TermColor.RESET )

if __name__ == '__main__':
    check_pip_package("platform")

    print(DIR_TEST)
    mkdir(DIR_TEST)
