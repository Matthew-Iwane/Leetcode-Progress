class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        counter = [[] for _ in range(len(nums) + 1)] # fix index 0 by adding 1

        for n in nums:
            count[n] = count.get(n, 0) + 1
        for key, value in count.items():
            counter[value].append(key)


        res = []
        # append going backwards
        for i in range(len(counter)-1, 0, -1):
            for n in counter[i]:
                res.append(n)

                if len(res) == k:
                    return res
        
        return res