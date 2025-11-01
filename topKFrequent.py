from collection import Counter
class solution:
  def topKFrequent(self, nums: List[int], k: int) ->List[int]:
     c=Counter(nums)
     min_heap = []
     for num,freq in c.items():
         heappush(min_heap,(freq,num))
         if len(min_heap)> k:
             heappop(min_heap)
      return [iitems[1] for item in min_heap]
  
