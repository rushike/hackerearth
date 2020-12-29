"""
https://www.hackerearth.com/challenges/competitive/june-circuits-20/algorithm/inverted-cells-83eae42d/

Input : 
5 5
..#..
#...#
#...#
....#
.##..
[[0 0 1 0 0]
 [1 0 0 0 1]
 [1 0 0 0 1]
 [0 0 0 0 1]
 [0 1 1 0 0]]
# --> 1
. --> 0

Output : 
0 0 1 1 1 
1 0 1 1 1 
1 1 1 1 1 
1 1 1 0 1 
1 1 1 0 0  


8 8
..#....# 
..#....# 
......## 
#...#.#. 
....#... 
.##..##. 
.##..##. 
........

Output
0 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 0 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 0
"""
import numpy
N, M = (int(v) for v in input().split())

mat = numpy.zeros((N, M), dtype=int)

for i in range(N):
    st = input()
    # print(st)
    mat[i] = [int((1 if v == "#" else 0)) for v in st.strip()]

# print(mat)

def down_up_inverted_path(mat, aux, N, M, col, row):
    # print("on node : ", N, M)
    aux[N + 1, M + 1] += 1     
    # col[N] += 1
    # row[M] += 1
    if not M < mat.shape[1] or not N < mat.shape[0] : return
    if M != 0 and mat[N, M - 1] == 0: # non block up 
        down_up_inverted_path(mat, aux, N, M - 1, col, row)            
    if N != 0 and mat[N - 1, M] == 0: # non block left                
        down_up_inverted_path(mat, aux, N - 1 , M, col, row)

def up_down_inverted_path(mat, aux, N, M, col, row):
    # print("on node : ", N, M)
    aux[N + 1, M + 1] += 1
    # col[N] += 1
    # row[M] += 1
    # print(aux)  
    # 0 state means reachable           
    if M != (mat.shape[0] - 1) and mat[N, M + 1] == 0: # non block up 
        up_down_inverted_path(mat, aux, N, M + 1, col, row)            
    if N != (mat.shape[1] - 1) and mat[N + 1, M] == 0: # non block left                
        up_down_inverted_path(mat, aux, N + 1 , M, col, row)

def solve2(aux, res):
    N, M = res.shape
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if aux[i, j] == 0:
                res[i - 1, j - 1] = 1
            elif i + 1 != N + 1 and j + 1 != M + 1 and j - 1 != 0 and i - 1 != 0 and (aux[i + 1, j - 1] != 0 or aux[i - 1 , j + 1 ] != 0):
                res[i - 1, j - 1] = 1            
            # if i - 1 != 0 and j + 1 != M and (aux[i - 1, j] != 0 or aux[i, j + 1 ] != 0):
            #     pass

def solve3(aux, res):
    N, M = res.shape
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if aux[i, j] == 0:
                res[i - 1, j - 1] = 1
            elif i + 1 != N + 1 and j + 1 != M + 1 and j - 1 != 0 and i - 1 != 0 and (aux[i + 1, j - 1] != 0 or aux[i - 1 , j + 1 ] != 0 ):
                res[i - 1, j - 1] = 1    

def solve(aux, res, col):
    N, M = res.shape
    # print(N, M)
    for i in range(aux.shape[0] - 1, 0, -1):
        MAX = None
        for j in range(aux.shape[1] - 1, 0, -1):
            # print(i, j , res[i - 1 : , j - 1 : ])        
            if i < N and res[i, j - 1] == 1 and aux[i + 1, j] != 0:
                res[i - 1, j - 1] = 1
            elif j < M and res[i - 1, j] == 1 and aux[i, j + 1] != 0:
                res[i - 1, j - 1] = 1
            elif j < M and aux[i, j + 1] - aux[i, j] > 0:
                res[i - 1, j - 1] = 1
            elif  i < N and aux[i + 1, j ] - aux[i, j] > 0:
                res[i - 1, j - 1] = 1
            if aux[i, j] == 0:
                res[i - 1, j - 1] = 1                                 
            elif j < M and i < N and aux[i + 1, j] - aux[i, j] == 0 and aux[i, j + 1] - aux[i, j] == 0 and aux[i, j] != 0:
                ret = dfs_sub(aux[i : , j : ].copy())
                # print(i, j, "  rest : ", ret)
                if ret:
                    res[i - 1, j - 1] = 1
                else :
                    res[i - 1, j - 1] = 0
            
    res[-1, -1] = 0

    

def row_col(aux, col, row):    
    for i in range(aux.shape[0]):
        counter = False
        for j in range(1, aux.shape[1]):
            if aux[i, j - 1] == 0 and aux[i, j] != 0:
                col[i] += 1
                
def dfs_sub(aux_sl):
    # print(aux_sl)
    def get_children(point):
        c = []
        if point[0] + 1 != aux_sl.shape[0] and aux_sl[(point[0] + 1, point[1])] != 0: 
            # print("poin x : ", aux_sl[(point[0] + 1, point[1])])
            c.append((point[0] + 1, point[1]))
        else: c.append(None)

        if point[1] + 1 != aux_sl.shape[1] and aux_sl[(point[0], point[1] + 1)] != 0: 
            # print("poin y : ", aux_sl[(point[0], point[1] + 1)])
            c.append((point[0], point[1] + 1))
        else: c.append(None)
        return c
    sub = aux_sl[0, 0]
    dfs_stack = []
    dfs_stack.append((0, 1))
    dfs_stack.append((1, 0))
    while len(dfs_stack) > 0:
        crawler = dfs_stack.pop()
        # print(crawler, dfs_stack)
        if crawler[0] == aux_sl.shape[0] or crawler[1] == aux_sl.shape[1]:
            break
        aux_sl[crawler] -= sub
        
        children = get_children(crawler)
        # print("c: ", children)
        if children[0] and children[0] not in dfs_stack: 
            dfs_stack.append(children[0])
        if children[1] and children[1] not in dfs_stack:
            dfs_stack.append(children[1])
    # print(aux_sl)            
    return aux_sl[-1, -1]
        

aux = numpy.zeros((N + 1, M + 1), dtype=int)
# col = numpy.zeros(N)
row = numpy.zeros(M)
col = numpy.zeros(aux.shape[1])
# aux[:, 0] = 0
# aux[0, :] = 0
# print(mat)
# row_col(col, row)

# down_up_inverted_path(mat, aux, mat.shape[0] - 1, mat.shape[1] - 1, col, row)
# print(aux[0:, 0:])
# aux = numpy.zeros((N + 1, M + 1), dtype=int)

up_down_inverted_path(mat, aux, 0, 0, col, row)
# print(aux[0:, 0:])
res = numpy.zeros((N, M), int)
# x_diff = numpy.diff(aux, 1, 1)
# y_diff = numpy.diff(aux, 1, 0)
# print(x_diff)
# print(y_diff)
# a_diff = x_diff + y_diff
# print(a_diff)
# ret = dfs_sub(aux[6:, 4:].copy())
# print(ret)
# print(aux)
# row_col(aux, col, row)
solve(aux, res, col)
# max_b = max_build(aux)
# print(max_b)
# print(row)
# print(col)
# print(res)

print("\n".join([" ".join([ str(v) for v in res[i, :]]) for i in range(res.shape[0])]))