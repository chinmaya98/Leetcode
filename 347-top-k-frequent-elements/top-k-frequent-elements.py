class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Initialize an empty dictionary count to store the frequency of each number.
        count = {} 

        #Create a list of empty lists (buckets), where freq[i] will hold numbers that appear exactly i times.
        freq = [[] for i in range(len(nums)+1)]

        #Loop over each number in nums and build the frequency count dictionary.
        for n in nums:
            count[n] = 1 + count.get(n,0)

        #For each (num, cnt) pair in count, append the number to freq[cnt].
        for n, c in count.items():
            freq[c].append(n)
        
        
        #Initialize the result list that will store the top k frequent elements.
        res = []

        #Loop backwards from highest frequency to lowest (from 6 to 1).
        for i in range(len(freq)-1,0,-1):



            #Go through each bucket:Add numbers to the result list resIf res contains k elements, return it.
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        
        