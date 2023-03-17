def minMaxAvg(testList):
    """
    최소 최대값을 뺀 평균
    parameter : testList = 리스트
    return: 리스트내 값에서 최소 최댓값을 뺀 평균을 반환한다
    """

#testList=[2,5,3,7,8,4,1,6,9]
minValue = min(testList)
maxValue = max(testList)
print("최대값{} 최솟값{}".format(minValue,maxValue) )

testList.remove(minValue)
testList.remove(maxValue)

average = 0

if len(testList) !=0:
    average =sum(testList)/len(testList)
else :
    pass
return average