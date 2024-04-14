
from dataclasses import dataclass

@dataclass
class Movie:
  name: str
  year: float
 
  def getStr(self):
    return f"{self.name} ({self.year})"
