import math

def distance_simple(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

class Position:
    def __init__(self, x = 0, y = 0):
        self.x= x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, Position):
            return Position(self.x + other.x, self.y + other.y)
        return self
    
    def __eq__(self, other):
        if isinstance(other, Position):
            return int(self.x) == int(other.x) and int(self.y) == int(other.y)
        return self
    
    def afficher(self):
        print(f"Position (x={self.x}, y={self.y})")
    
    def distance_vers(self, other):
        if isinstance(other, Position):
            return distance_simple(self.x, self.y, other.x, other.y)
        return self

pos1 = Position(1, 4)
pos1.afficher() # (x=0, y=0)
pos2 = Position(3, 4)
pos2.afficher() # (x=3, y=4)
pos3 = pos1 + pos2
pos3.afficher() # (x=3, y=4)

pos1 = Position(0, 0)
pos2 = Position(3, 4)
assert pos1.distance_vers(pos2) == 5.0
print("Test distance OK")