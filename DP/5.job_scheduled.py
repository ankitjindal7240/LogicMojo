class job:
    def __init__(self,start,end,proft):
        self.start=start
        self.end=end
        self.profit=proft

jobs=[ job(1,2,50),job(3,1,20), job(6,19,100), job(2,100,200) ]
jobs=sorted(jobs,key=lambda x:x.profit)
print(jobs[0].profit)

def max_profit(jobs):
    arr=[0]*len(jobs)
    arr[0]=jobs[0].profit
    for i in range(1,len(jobs)):
        for j in range(i):
            if jobs[i].start>jobs[j].end:
                pro=arr[j]+jobs[i].profit
                arr[i]=max(arr[i],pro)
    return arr[-1]
print(max_profit(jobs))

