
def GetNumberOfK(data,k):
    if not data: return 0
    def bisearch(data,k):
        l,r = 0, len(data)-1
        while l < r:
            mid = (r-l) //2 + l
            if data[mid] < k:
                l = mid + 1
            else:
                r = mid -1
        return l    
    r = bisearch(data,k+0.5) - bisearch(data,k-0.5)
    return r + 1 if data[0] == k else r



print(GetNumberOfK([1,2,3,3,3,3,4,5],3))            
# [1,2,3,3,3,3,4,5]
# [3,3,3,3,4,5]