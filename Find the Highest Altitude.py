class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        start, altitude = 0, 0
        for i in gain:
            altitude+=i
            start = max(start, altitude)
        return start
        
