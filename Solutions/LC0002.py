class Solution:
    def majorityElement(self, nums):
        output = set()
        hash_table = {}
        for i in nums:
            if i in hash_table:
                hash_table[i] += 1
                if hash_table[i] > (len(nums)//3):
                    output.add(i)
            else:
                hash_table[i] = 1
                if hash_table[i] > (len(nums)//3):
                    output.add(i)
        return list(output)

nums = [1,2]
sol = Solution()
print(sol.majorityElement(nums))