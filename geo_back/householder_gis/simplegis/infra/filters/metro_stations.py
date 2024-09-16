from dataclasses import dataclass


@dataclass
class MetroStationsFilters:
    model: str | None = None
    search: str | None = None
