from pydantic import BaseModel, Field

class Persona(BaseModel):
    nombre: str = Field(...,min_length=2, max_length=50)
    documento: str = Field(...,min_length=2, max_length=50)
p1 = Persona(nombre="Juan",documento="12345")

print(p1)

p2 = Persona(nombre="a",documento="12")
print (p2)