class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_len = len(ring)
        key_len = len(key)

        # Find the minimum steps between two indexes of ring
        def count_steps(curr, next):
            steps_between = abs(curr - next)
            steps_around = ring_len - steps_between
            return min(steps_between, steps_around)

        # Find the minimum number of steps to spell the keyword
        def try_lock(ring_index, key_index, min_steps):
            # If we reach the end of the key, it has been spelled
            if key_index == len(key):
                return 0
            # For each occurrence of the character k[key_index] in ring
            # calculate the minimum steps from the ring_index of ring
            for i in range(len(ring)):
                if ring[i] == key[key_index]:
                    total_steps = count_steps(ring_index, i) + 1 + \
                                              try_lock(i, key_index + 1, inf)
                    min_steps = min(min_steps, total_steps)
            return min_steps
    
        return try_lock(0, 0, inf)
