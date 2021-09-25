str="aabababaxx"
cuts=[0 for i in range(len(str))]
palind=[[0 for i in range(len(str))] for j in range(len(str))]
for i in range(len(str)):
    palind[i][0]=str[i]
    palind[0][i]=str[i]
for item in palind:
    print(item)

for column in range(len(str)):
    for row in range(column+1):
        if str[row]==str[column] :
            pass
