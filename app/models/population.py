from pydantic import BaseModel


# Modelo base simple
class PopulationRecord(BaseModel):
    year: int
    population: int
    nation: str

