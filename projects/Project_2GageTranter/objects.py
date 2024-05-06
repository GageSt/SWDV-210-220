from dataclasses import dataclass

@dataclass
class Player:
  name:str = ""
  position: str = ""
  bats: str = ""
  hits: str = ""
  avg: float = 0.0

  def getStr(self):
    return f"{self.name:20s} {self.position:5s} {self.bats:5s} {self.hits:5s} {self.avg}"
  
@dataclass
class Position:
  pos:str = "" 

  def getPos(self):
    return f"{self.pos}"