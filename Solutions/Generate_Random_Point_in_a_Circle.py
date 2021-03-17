import random
import math
from typing import List
class Solution:
    radius = 0
    x_center = 0
    y_center = 0

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        length = math.sqrt(random.random())*self.radius
        deg = random.random()*2*math.pi
        return [self.x_center + math.cos(deg)*length,self.y_center + math.sin(deg)*length]
