from typing import Any

def autocontrast(image, cutoff: int = ..., ignore: Any | None = ..., mask: Any | None = ..., preserve_tone: bool = ...): ...
def colorize(image, black, white, mid: Any | None = ..., blackpoint: int = ..., whitepoint: int = ..., midpoint: int = ...): ...
def pad(image, size, method=..., color: Any | None = ..., centering=...): ...
def crop(image, border: int = ...): ...
def scale(image, factor, resample=...): ...
def deform(image, deformer, resample=...): ...
def equalize(image, mask: Any | None = ...): ...
def expand(image, border: int = ..., fill: int = ...): ...
def fit(image, size, method=..., bleed: float = ..., centering=...): ...
def flip(image): ...
def grayscale(image): ...
def invert(image): ...
def mirror(image): ...
def posterize(image, bits): ...
def solarize(image, threshold: int = ...): ...
def exif_transpose(image): ...
