# 字符串排序演示代码

def demonstration():
    s = "bca"
    print(f"原字符串: {s}")
    
    # 第一步：得到排序后的字符列表
    sorted_list = sorted(s)
    print(f"第一步 (sorted): {sorted_list}")
    
    # 第二步：将列表转回字符串
    sorted_str = "".join(sorted_list)
    print(f"第二步 (join): {sorted_str}")

if __name__ == "__main__":
    demonstration()
