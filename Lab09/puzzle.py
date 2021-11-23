# Prog-06: 8-Puzzle
# Fill in your ID & Name
# ...
# Declare that you do this by yourself

def is_goal(node): 
    return node[:-1] == \
           list(range(1,len(node)-1))+[0]

def insert_all(node, fringe):
    n = len(node)
    children = gen_successors(node)
    for i in range(0,len(children),n):
        fringe.append(children[i:i+n])

def bfs(board):
    start_node = board + ['']
    fringe = [start_node]
    while True:
        if len(fringe) == 0:
            break
        front = fringe[0]
        fringe = fringe[1:]
        if is_goal(front):
            return front[-1]
        insert_all(front,fringe) 
    return ''

def print_successors(s):
    N = 1
    for e in s:
        if type(e) is str: break
        N += 1
    for i in range(0,len(s),N):
        print(s[i:i+N])
#---------------------------------------
def gen_successors(node):
    # node = [1,0,3,4,2,5,7,8,6,'LR']
    # successors =[1,2,3,4,0,5,7,8,6,'LRD',0,1,3,4,2,5,7,8,6,'LRL',1,3,0,4,2,5,7,8,6,'LRR']
    successors = []
    nub = 0
    arr = [[11]*5 for i in range(5)]
    for i in range(1,4) :
        for j in range(1,4) :
            arr[i][j] = node[nub]
            nub += 1
    # print(arr)

    def find_zero(arr) :
        for i in range(5) :
            for j in range(5) :
                if arr[i][j] == 0 :
                    row = i
                    column = j
        return row,column

    rind,cind = find_zero(arr)
    # print(rind,cind)
    if arr[rind-1][cind] != 11 : #U
        res = arr.copy()
        tmp = res[rind-1][cind]
        res[rind-1][cind] = 0
        res[rind][cind] = tmp
        print(res)
        # successors.append(res)

    if arr[rind+1][cind] != 11 : #D
        res1 = arr.copy()
        tmp = res1[rind+1][cind]
        res1[rind+1][cind] = 0
        res1[rind][cind] = tmp
        print(res1)
        # successors.append(res)

    if arr[rind][cind+1] != 11 : #R
        res2 = arr.copy()
        tmp = res2[rind][cind+1]
        res2[rind][cind+1] = 0
        res2[rind][cind] = tmp
        print(res2)
        # successors.append(res)

    if arr[rind-1][cind] != 11 : #L
        res3 = arr.copy()
        tmp = res3[rind][cind-1]
        res3[rind][cind-1] = 0
        res3[rind][cind] = tmp
        print(res3)
        # successors.append(res)
            
    return successors 
#------------------------------------------
def print_moves(board, moves):
    # bonus function: optional


    return
#-----------------------------------------
board = [4,1,3,2,0,6,7,8,5]
s = gen_successors(board + ['UDR'])
print_successors(s)
moves = bfs(board)
print(moves)
print_moves(board, moves) # optional bonus