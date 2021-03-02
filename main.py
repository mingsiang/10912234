from mymath import myStatistics
data=[]
for i in range (1,6):
 data.append(float(input('第'+str(i)+'個')))
print(myStatistics.myMean(data))
