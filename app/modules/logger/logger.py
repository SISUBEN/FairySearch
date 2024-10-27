# import datetime
# import logging
# import os
# import sys

# from rich.console import Console
# from rich.highlighter import NullHighlighter
# from rich.logging import RichHandler
# from rich.rule import Rule
# from rich.logging import RichHandler

# # Logger init
# logger_debug = False
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG if logger_debug else logging.INFO)
# file_formatter = logging.Formatter(
#     fmt="%(asctime)s [%(levelname)s] %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S",
# )
# console_formatter = logging.Formatter(
#     fmt="%(asctime)s │ %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
# )
# # cd to root
# os.chdir(os.path.join(os.path.dirname(__file__), "../../"))
# script_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
# logger.info("Logger") 
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
logger_debug = False
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG if logger_debug else logging.INFO)
file_formatter = logging.Formatter(
    fmt="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
console_formatter = logging.Formatter(
    fmt="%(asctime)s │ %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
# cd to root
os.chdir(os.path.join(os.path.dirname(__file__), "../../"))
script_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]

# 创建RichHandler对象
rich_handler = RichHandler(
    show_time=True,
    show_level=True,
    show_path=False,
    highlighter=NullHighlighter(),
)

# 将RichHandler对象添加到logger中
logger.addHandler(rich_handler)

# 设置日志格式
rich_handler.setFormatter(console_formatter)

# 记录日志
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


def hr(title, level=3):
    title = str(title).upper()
    if level == 1:
        logger.rule(title, characters="═")
        logger.info(title)
    if level == 2:
        logger.rule(title, characters="─")
        logger.info(title)
    if level == 3:
        logger.info(f"[bold]<<< {title} >>>[/bold]", extra={"markup": True})
    if level == 0:
        logger.rule(characters="═")
        logger.rule(title, characters=" ")
        logger.rule(characters="═")


def rule(title="", *, char="─", style="rule.line", end="\n", align="center"):
    rule = Rule(title=title, characters=char, style=style, end=end, align=align)
    print(rule)


def attr(name, text):
    logger.info("[%s] %s" % (str(name), str(text)))


def attr_align(name, text, front="", align=22):
    name = str(name).rjust(align)
    if front:
        name = front + name[len(front) :]
    logger.info("%s: %s" % (name, str(text)))


logger.hr = hr
logger.attr = attr
logger.attr_align = attr_align
logger.set_file_logger = set_file_logger
logger.rule = rule
logger.log_file: str  # type: ignore

# logger.hr("Logger") 
