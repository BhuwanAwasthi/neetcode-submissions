class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        # Count frequency
        for num in nums:

            if num in freq:
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1

        ans = []

        # Find the largest frequency k times
        for i in range(k):

            maximum = 0
            number = None

            for key in freq:

                if freq[key] > maximum:
                    maximum = freq[key]
                    number = key

            ans.append(number)

            freq[number] = -1

        return ans