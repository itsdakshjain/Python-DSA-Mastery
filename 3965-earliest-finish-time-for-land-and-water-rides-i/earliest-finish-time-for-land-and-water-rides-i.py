class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        best_land_first = min(s + d for s, d in zip(landStartTime, landDuration))
        best_water_first = min(s + d for s, d in zip(waterStartTime, waterDuration))
        
        land_then_water = min(max(best_land_first, s) + d for s, d in zip(waterStartTime, waterDuration))
        water_then_land = min(max(best_water_first, s) + d for s, d in zip(landStartTime, landDuration))
        
        return min(land_then_water, water_then_land)