from enum import Enum


class BoroughEnum(Enum):
    BRONX = 'Bronx'
    BROOKLYN = 'Brooklyn'
    MANHATTAN = 'Manhattan'
    QUEENS = 'Queens'
    STATEN_ISLAND = 'Staten Island'


BOROUGH_LIST = [b.value for b in BoroughEnum]
