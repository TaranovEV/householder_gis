from dataclasses import dataclass

from geo_back.householder_gis.simplegis.domain.values.base import BaseValueObject


@dataclass(frozen=True)
class Longitude(BaseValueObject[float]):
    def validate(self):
        ...

    def as_generic_type(self) -> float:
        return float(self.value)


@dataclass(frozen=True)
class Latitude(BaseValueObject[float]):
    def validate(self):
        ...

    def as_generic_type(self) -> float:
        return float(self.value)
