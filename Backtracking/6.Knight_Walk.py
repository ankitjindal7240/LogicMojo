n=int(input("dimension of board"))
board=[[0 for i in range(n)] for i in range(n)]

# all possible movements for the knight
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]


class Node:
    def __init__(self,x,y,dist):
        self.x=x
        self.y=y
        self.dist=dist

def is_suitable(position):
    if 0<=position.x <n and 0<=position.y<n and board[position.x][position.y]==0:
        return True
def walk(knightpos,targetpos):
    queue = []
    queue.append(knightpos)
    while len(queue)>0:
        cell=queue.pop(0)
        if cell.x==targetpos.x and cell.y==targetpos.y:
            return cell.dist
        for i in range(8):
            x=cell.x +dx[i]
            y=cell.y+dy[i]

            next_cell=Node(x,y,cell.dist +1)
            if is_suitable(next_cell):
                board[next_cell.x][next_cell.y]=1
                queue.append(next_cell)

knightpos = Node(1,1,0)
targetpos =Node(29,29,0)
print(walk(knightpos,targetpos))


