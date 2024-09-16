from dataclasses import dataclass


@dataclass(eq=False)
class BaseAppException(Exception):
    @property
    def message(self):
        return "Application exception occurred"
