from pydantic import BaseModel, PositiveInt, validator
from enum import Enum, IntEnum
from typing import Union

class Sex(str, Enum):
    MALE = "Male"
    FEMALE = "Female"

class Smoker(str, Enum):
    YES = "Yes"
    No = "No"

class Region(str, Enum):
    SOUTH_WEST = "South West"
    SOUTH_EAST = "South East"
    NORTH_WEST = "North West"
    NORTH_EAST = "North East"

class PersonalInfo(BaseModel):
    age: PositiveInt
    sex: Union[Sex, int]
    BMI: float
    children: PositiveInt
    smoker: Union[Smoker, int]
    region: Union[Region, int]
    
    @validator('sex')
    def validate_sex(cls, value):
        if value == Sex.MALE: return 0
        if value == Sex.FEMALE: return 1
           
        
    @validator('smoker')
    def validate_smoker(cls, value):
        if value == Smoker.YES: return 1
        if value == Smoker.No: return 0
        
    @validator('region')
    def validate_region(cls, value):
        if value == Region.SOUTH_WEST: return 0
        if value == Region.SOUTH_EAST: return 1
        if value == Region.NORTH_WEST: return 2
        if value == Region.NORTH_EAST: return 3
        
    
    
    
    