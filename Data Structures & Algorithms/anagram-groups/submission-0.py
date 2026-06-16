class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for v in strs:
            count = [0]*26 # a...z 
            
            for i in v:
                count[ord(i)-ord("a")] +=1  # ord is to give numerical value and we put in that position 1 to track the occurance 
            
            res[tuple(count)].append(v)     # tuple is immutable or unchangeable and dic need immutable.
                                            # append we can use because of defaultdict.
        
        return list(res.values())           # takes the values and make it a list then return