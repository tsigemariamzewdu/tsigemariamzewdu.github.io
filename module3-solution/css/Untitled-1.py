class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        
        
solution=Solution()
print(solution.removeDuplicates([1,1,1,2,2,3]))