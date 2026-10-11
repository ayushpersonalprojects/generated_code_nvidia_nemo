from math import gcd
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        max_points = 0
        
        for i in range(n):
            slopes = {}
            duplicate = 0
            xi, yi = points[i]
            
            for j in range(i + 1, n):
                xj, yj = points[j]
                dx = xj - xi
                dy = yj - yi
                
                if dx == 0 and dy == 0:
                    duplicate += 1
                    continue
                
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                
                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:
                    if dy < 0:
                        dy = -dy
                
                slopes[(dx, dy)] = slopes.get((dx, dy), 0) + 1
            
            current_max = duplicate + 1
            for count in slopes.values():
                current_max = max(current_max, count + duplicate + 1)
            
            max_points = max(max_points, current_max)
        
        return max_points