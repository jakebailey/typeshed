from typing import Any

class PSDraw:
    fp: Any
    def __init__(self, fp: Any | None = ...) -> None: ...
    isofont: Any
    def begin_document(self, id: Any | None = ...) -> None: ...
    def end_document(self) -> None: ...
    def setfont(self, font, size) -> None: ...
    def line(self, xy0, xy1) -> None: ...
    def rectangle(self, box) -> None: ...
    def text(self, xy, text) -> None: ...
    def image(self, box, im, dpi: Any | None = ...) -> None: ...

EDROFF_PS: str
VDI_PS: str
ERROR_PS: str
