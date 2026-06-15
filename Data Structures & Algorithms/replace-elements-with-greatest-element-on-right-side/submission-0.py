class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        a = -1
        for i in range(len(arr)-1,-1,-1):
            if arr[i] > a:
                b = arr[i]
            arr[i] = a
            a = b
        
        return arr


        