# Problem: The Number of the Smallest Unoccupied Chair - https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Create a list of tuples (arrival time, leaving time, original index)
        times = [(a, l, i) for i, (a, l) in enumerate(times)]
        times.sort()  # Sort by arrival time
        
        n = len(times)  # Number of friends
        
        # Initialize a heap of free chairs (indices)
        freechairs = list(range(n))
        heapify(freechairs)  # Efficient chair allocation using a heap
        
        usedchairs = []  # Min-heap to track used chairs with their leaving times

        for a, l, i in times:
            # Free up chairs for friends who have left before current arrival
            while usedchairs and usedchairs[0][0] <= a:
                _, idx = heappop(usedchairs)  # Remove chair of friend who is leaving
                heappush(freechairs, idx)  # Add freed chair back to available chairs
            
            cur = heappop(freechairs)  # Allocate the next available chair
            
            if i == targetFriend:
                return cur  # Return the chair index for the target friend
            
            heappush(usedchairs, (l, cur))  # Mark chair as used with leaving time
