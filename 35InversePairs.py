
def InversePairs(data):
    count = 0
    for i in reversed(range(len(data))):
        for j in range(i):
            if data[j] > data[i]:
                count += 1
    return count % 1000000007

count = 0
class Solution:
    def InversePairs(self, data):
        global count
        def MergeSort(lists):
            global count
            if len(lists) <= 1:
                return lists
            num = int( len(lists)/2 )
            left = MergeSort(lists[:num])
            right = MergeSort(lists[num:])
            r, l=0, 0
            result=[]
            while l<len(left) and r<len(right):
                if left[l] < right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
                    count += len(left)-l
            result += right[r:]
            result += left[l:]
            return result
        MergeSort(data)
        return count%1000000007        
print(InversePairs([1,2,3,4,5,6,7,0]))
