from dataclasses import dataclass

from geo_back.householder_gis.simplegis.domain.exceptions.base import BaseAppException


@dataclass(kw_only=True)
class NegativeValueFieldException(BaseAppException):
    field_name: str

    @property
    def message(self):
        return f"{self.field_name} can not be negative"
