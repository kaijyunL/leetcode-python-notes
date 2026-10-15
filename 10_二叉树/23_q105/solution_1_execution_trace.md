那我们先不讲递归定义，只按方法一的代码顺序，把这个例子实际跑一遍：

```text
preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]
```

关键是这一行：

```python
root.left = self.buildTree(...)
```

Python 会先把右边的 `buildTree(...)` 完整执行完，拿到返回的节点后，才赋给 `root.left`。调用期间，当前这次函数暂停着，自己的 `root` 等变量还保留着。

```text
调用 F1：buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
  F1 创建值为3的节点
  根3在中序里的位置是1，left_size = 1

  执行 F1 的 root.left = buildTree(...)

    调用 F2：buildTree([9], [9])
      F2 创建值为9的节点，left_size = 0

      执行 F2 的 root.left = buildTree([], [])
        空 preorder -> 返回 None
      F2.left = None

      执行 F2 的 root.right = buildTree([], [])
        空 preorder -> 返回 None
      F2.right = None

      F2 返回值为9的节点

  F1 收到返回的值为9的节点
  F1.left = 值为9的节点

  现在才执行 F1 的 root.right = buildTree(...)

    调用 F3：buildTree([20, 15, 7], [15, 20, 7])
      F3 创建值为20的节点
      根20在当前中序里的位置是1，left_size = 1

      执行 F3 的 root.left = buildTree([15], [15])

        调用 F4：buildTree([15], [15])
          F4 创建值为15的节点
          F4 的左右子调用都拿到 None
          F4 返回值为15的节点

      F3.left = 值为15的节点

      执行 F3 的 root.right = buildTree([7], [7])

        调用 F5：buildTree([7], [7])
          F5 创建值为7的节点
          F5 的左右子调用都拿到 None
          F5 返回值为7的节点

      F3.right = 值为7的节点
      F3 返回值为20的节点

  F1 收到返回的值为20的节点
  F1.right = 值为20的节点

F1 返回值为3的节点
ans 指向值为3的节点
```

整个过程中，F1 没有消失：它在等待左子树时暂停；拿到值为 `9` 的节点后，接着执行右子树；左右节点都接上以后，才返回值为 `3` 的根节点。

最后拼出的树是：

```text
      3
     / \
    9  20
       / \
      15  7
```
