class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(list(map(list, zip(range(len(nums)), nums))), key = lambda x: x[1])
        dic = {}
        for i in nums:
            if i[1] in dic:
                dic[i[1]][0] += 1
                dic[i[1]][1].append(i[0])
            else:
                dic[i[1]] = [1]
                dic[i[1]].append([i[0]])
        for i in dic:
            dic[i][0] -= 1
            val1 = dic[i][1].pop(0)
            if target - i in dic:
                if dic[target-i][0]>0:
                    val2 = dic[target-i][1].pop(0)
                    return([val1, val2])
        