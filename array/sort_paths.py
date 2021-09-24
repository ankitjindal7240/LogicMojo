tickets ={"SFO": "EWR" ,"SJC": "LAX" ,"DFW": "SJC","EWR":"OAK" ,"LAX": "SFO"}

total_stops= len(tickets)+1
for key in tickets:
    if key not in  tickets.values():
        start="key"
        break
ans=[]
ans.append(key)
while len(ans)<total_stops:
    ans.append(tickets[ans[-1]])
print(ans)
