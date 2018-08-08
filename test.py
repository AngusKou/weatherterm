from weatherterm.core import Forecast

from datetime import date
from enum import Enum, unique


@unique
class Gender(Enum):
    A = 'male'
    B = 'female'


print(Gender.A)

for k, v in Gender.__members__.items():
    print(k, v)
