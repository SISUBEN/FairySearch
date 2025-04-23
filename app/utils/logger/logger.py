import datetime
import logging
import os
import sys

from rich.console import Console
from rich.highlighter import NullHighlighter
from rich.logging import RichHandler
from rich.rule import Rule
from rich.logging import RichHandler

# Logger init
logger_debug = True

logger = logging.getLogger(__name__)
root_dir = os.path.abspath(os.path.join(os.getcwd(), "../../../"))
file = logging.FileHandler(f"{root_dir}\log.txt", encoding="utf-8")
logger.setLevel(logging.DEBUG if logger_debug else logging.INFO)
file_formatter = logging.Formatter(
    fmt="%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
console_formatter = logging.Formatter(fmt="[%(filename)s:%(lineno)d] %(message)s", datefmt="%Y-%m-%d %H:%M:%S") # debug mode
# console_formatter = logging.Formatter(fmt="| %(message)s", datefmt="%Y-%m-%d %H:%M:%S") # release mode
file.setFormatter(file_formatter)
# cd to root
os.chdir(root_dir)  # os.path.join(os.path.dirname(__file__), "../../../")
script_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
console = Console()
# Creat RichHandler obj
rich_handler = RichHandler(
    show_time=True,
    show_level=True,
    show_path=False,
    highlighter=NullHighlighter(),
)
rich_handler.setFormatter(console_formatter)
# add RichHandler to logger
logger.addHandler(rich_handler)

# setting formatter


def _set_file_logger(name=script_name):
    if "_" in name:
        name = name.split("_", 1)[0]
    log_file = f"./logs/{datetime.date.today()}_{name}.txt"
    try:
        file = logging.FileHandler(log_file, encoding="utf-8")
    except FileNotFoundError:
        os.mkdir("./logs")
        file = logging.FileHandler(log_file, encoding="utf-8")
    file.setFormatter(file_formatter)

    logger.handlers = [
        h
        for h in logger.handlers
        if not isinstance(h, (logging.FileHandler, RichHandler))
    ]
    logger.addHandler(file)
    logger.log_file = log_file


def set_file_logger(name=script_name):
    if "_" in name:
        name = name.split("_", 1)[0]
    log_file = f"./log/{datetime.date.today()}_{name}.txt"
    try:
        file = open(log_file, mode="a", encoding="utf-8")
    except FileNotFoundError:
        os.mkdir("./log")
        file = open(log_file, mode="a", encoding="utf-8")
    
    file_console = Console(
        file=file,
        no_color=True,
        highlight=False,
        width=119,
    )

    hdlr = RichHandler(
        console=file_console,
        show_path=False,
        show_time=False,
        show_level=False,
        rich_tracebacks=True,
        tracebacks_show_locals=True,
        tracebacks_extra_lines=3,
        highlighter=NullHighlighter(),
    )
    hdlr.setFormatter(file_formatter)

    logger.handlers = [
        h
        for h in logger.handlers
        if not isinstance(h, (logging.FileHandler, RichHandler))
    ]
    logger.addHandler(hdlr)
    logger.log_file = log_file



def attr(name, text):
    logger.info("[%s] %s" % (str(name), str(text)))

def attr_align(name, text, front="", align=22):
    name = str(name).rjust(align)
    if front:
        name = front + name[len(front) :]
    logger.info("%s: %s" % (name, str(text)))
    
def head(name, level=0):
    if level == 0:
        print(Rule(name))
    elif level == 1:
        print(Rule(name, style="bold"))
    elif level == 2:
        print(Rule(name, style="bold red"))
    elif level == 3:
        print(Rule(name, style="bold red on white"))


logger.head = head
logger.attr = attr
logger.attr_align = attr_align
logger.set_file_logger = set_file_logger
logger.log_file: str  # type: ignore

# logger.hr("Logger")
