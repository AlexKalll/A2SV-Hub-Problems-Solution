# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        total_cost = 0
        curr_tank = 0
        start_index = 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            curr_tank += gas[i] - cost[i]
            
            if curr_tank < 0:
                start_index = i + 1  
                curr_tank = 0  
        
        
        if total_gas < total_cost:
            return -1
        
        return start_index
