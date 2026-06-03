class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        def solve(start1, dur1, start2, dur2):
            rides1 = sorted([(start1[i], start1[i] + dur1[i]) for i in range(len(start1))])
            rides2 = sorted([(start2[j], dur2[j]) for j in range(len(start2))])
            
            m = len(rides2)
            start2_times = [r[0] for r in rides2]
            
            prefix_min_dur = [float('inf')] * m
            curr_min = float('inf')
            for i in range(m):
                curr_min = min(curr_min, rides2[i][1])
                prefix_min_dur[i] = curr_min
                
            suffix_min_end = [float('inf')] * m
            curr_min_end = float('inf')
            for i in range(m - 1, -1, -1):
                curr_min_end = min(curr_min_end, rides2[i][0] + rides2[i][1])
                suffix_min_end[i] = curr_min_end
                
            best_total = float('inf')
            
            for s1, f1 in rides1:
                idx = bisect_right(start2_times, f1)
                
                if idx > 0:
                    best_total = min(best_total, f1 + prefix_min_dur[idx - 1])
                    
                if idx < m:
                    best_total = min(best_total, suffix_min_end[idx])
                    
            return best_total

        option1 = solve(landStartTime, landDuration, waterStartTime, waterDuration)
        option2 = solve(waterStartTime, waterDuration, landStartTime, landDuration)
        
        return min(option1, option2)