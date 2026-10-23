def merge(intervals):
    if not intervals:
        return []
    intervals.sort()
    result=[intervals[0]]
    for start,end in intervals[1:]:
        last=result[-1]
        if start<=last[1]:
            if end>last[1]:
                last[1]=end
        else:
            result.append([start,end])
    return result
print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))
print(merge([[1,4],[0,4]]))
print(merge([]))