from rich.console import Console
import logging
from typing import Any, Callable
from rich.console import Console
from rich.logging import RichHandler

console: Console
pyw_name: str

class RichFileHandler(RichHandler):
    ...

class __logger(logging.Logger):
    def hr(
        self,
        title,
        level: int = 3,
    ) -> None: ...
    def attr(
        self,
        name,
        text,
    ) -> None: ...
    def attr_align(
        self,
        name,
        text,
        front="",
        align: int = 22,
    ) -> None: ...
    def set_file_logger(
        self,
        name: str = pyw_name,
    ) -> None: ...

logger: __logger
