class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        
        # returns [kelvin, farenheit]
        # kelvin = celsius + 273.15
        # farenheit = (celsius * 1.80) + 32
        
        return [(celsius + 273.15), ((celsius * 1.80) + 32)]