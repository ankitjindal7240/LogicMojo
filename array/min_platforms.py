arrival = [100, 140, 150, 200, 215, 400]
departure = [110, 300, 220, 230, 315, 600]
# station=[]
# l=len(station)
# for i in range(len(arrival)):
#     if l>len(station):
#         l=len(station)
#     station.append(i)
#     for j in range(i):
#         if station.__contains__(j) and departure[j]<arrival[i]:
#             station.pop(j.__index__())
# print(l)

departure.sort()
i=0
j=0
n=len(arrival)
max_paltform=0
current_platform=0
while i<n and j<n:
    if arrival[i]<departure[j]:
        i=i+1
        current_platform=current_platform+1
        if current_platform>max_paltform:
            max_paltform=current_platform

    else:
        current_platform=current_platform-1
        j=j+1
        
print(max_paltform)

