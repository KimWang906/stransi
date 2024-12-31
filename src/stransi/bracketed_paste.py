"""Bracketed paste mode instructions."""

from dataclasses import dataclass
from enum import Enum

from .instruction import Instruction

class BracketedPasteMode(Enum):
    """Bracketed paste mode."""
    PASTE_IN_BRACKET = 2004

@dataclass
class SetBracketedPaste(Instruction[BracketedPasteMode]):
    """Instruction to enable bracketed paste mode."""
    mode: BracketedPasteMode
    enabled: bool
