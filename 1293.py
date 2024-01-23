class Solution:
        def maxLength(self, arr: List[str]) -> int:
            # Use a list to make sure the data is changed in methods
            maxLength = [0]

            # Go to backTrack with initial state
            self.backTrack(arr, "", 0,maxLength)
            return maxLength[0]
        
        def isValid(self, current, new):
            # Check whether the new string is qualified to be added to the current string
            Set = set()
            for i in new:
                if i in Set:
                    return False
                Set.add(i)
                if i in current:
                    return False
            return True
        
        def backTrack(self, arr, current, start, maxLength):

            # Update the maximum length
            maxLength[0] = max(maxLength[0], len(current))

            for i in range(start, len(arr)):
                if not self.isValid(current, arr[i]):
                    continue

                # Assume the current string is added, recurse to the next
                # Basically, back track is similar to DFS
                # It tries every possible combination
                self.backTrack(arr, current + arr[i], i+1, maxLength)
