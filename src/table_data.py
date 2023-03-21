from dataclasses import dataclass, field
from typing import List
from enum import IntEnum


@dataclass
class Row:
    cells: List[str] = field(default_factory=list)


@dataclass
class Table:
    rows: List[Row] = field(default_factory=list)


class Column(IntEnum):
    WEBSITES = 0
    POPULARITY = 1
    FRONTEND = 2
    BACKEND = 3
    DATABASE = 4
    NOTES = 5
