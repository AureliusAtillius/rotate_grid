grid = [[".",".",".",".",".","."],
        [".","0","0",".",".","."],
        ["0","0","0","0",".","."],
        ["0","0","0","0","0","."],
        [".","0","0","0","0","0"],
        ["0","0","0","0","0","."],
        ["0","0","0","0",".","."],
        [".","0","0",".",".","."],
        [".",".",".",".",".","."]]

x= len(grid[0])
y=len(grid)
for i in range(0,x):
    line=[]
    for n in range(0,y):
        line.append(grid[n][i])
    print(*line,sep="")