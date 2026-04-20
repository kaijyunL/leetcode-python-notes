# 方法一：方向模拟法
def generateMatrix1(n):
    # 初始化一个 n x n 的矩阵，初始全为 0
    # 我们正好可以用 0 来作为判断条件：如果格子里的数字不是 0，说明这个格子已经填过了
    matrix = [[0] * n for _ in range(n)]
    
    # 获取数字的边界目标
    target = n * n
    
    # 定义四个方向：向右、向下、向左、向上
    # (行变化, 列变化)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 0  # 机器人的初始方向：向右
    
    # 机器人的初始位置，位于左上角
    row, col = 0, 0
    
    # 逐个填入数字，从 1 填到 n^2
    for num in range(1, target + 1):
        # 在当前格子填入数字
        matrix[row][col] = num
        
        # 预判断下一步走的位置
        next_row = row + directions[direction_index][0]
        next_col = col + directions[direction_index][1]
        
        # 接下来做一个关键检查：下一步是否合法？
        # 如果下一步遇到了矩阵越界，或者走到了已经填过非0数字的格子上，那说明机器人需要顺时针转弯了
        if not (0 <= next_row < n and 0 <= next_col < n and matrix[next_row][next_col] == 0):
            # 顺时针转弯操作。用模 4 来实现四个方向的循环切换
            direction_index = (direction_index + 1) % 4
            # 既然转了方向，现在重新计算一下新方向对应的下一步位置
            next_row = row + directions[direction_index][0]
            next_col = col + directions[direction_index][1]
            
        # 机器人实际走到了合法的新位置，等待下一个循环中进行填充
        row, col = next_row, next_col
        
    return matrix

if __name__ == "__main__":
    n = 3
    print(f"n = {n} 的螺旋矩阵 (方向模拟法):")
    res = generateMatrix1(n)
    for r in res:
        print(r)
