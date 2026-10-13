# q236 方法二执行过程

```text
          3
        /   \
       5     1
      / \   / \
     6   2 0   8
        / \
       7   4

p = node(6)
q = node(4)
```

```python
p = nodes[6]
q = nodes[4]
ans = Solution().lowestCommonAncestor(root, p, q)
```

```text
01 CALL F1(root=3, p=6, q=4)
02 F1: root is None -> False
03 F1: root is p or root is q -> False
04 F1: left_result = CALL F2(root=5, p=6, q=4)
    05 F2: root is None -> False
    06 F2: root is p or root is q -> False
    07 F2: left_result = CALL F3(root=6, p=6, q=4)
        08 F3: root is None -> False
        09 F3: root is p or root is q -> True
        10 RETURN F3 -> node(6)
    11 F2: left_result = node(6)
    12 F2: right_result = CALL F4(root=2, p=6, q=4)
        13 F4: root is None -> False
        14 F4: root is p or root is q -> False
        15 F4: left_result = CALL F5(root=7, p=6, q=4)
            16 F5: root is None -> False
            17 F5: root is p or root is q -> False
            18 F5: left_result = CALL F6(root=None, p=6, q=4)
                19 F6: root is None -> True
                20 RETURN F6 -> None
            21 F5: left_result = None
            22 F5: right_result = CALL F7(root=None, p=6, q=4)
                23 F7: root is None -> True
                24 RETURN F7 -> None
            25 F5: right_result = None
            26 F5: left_result is not None and right_result is not None -> False
            27 F5: left_result is not None -> False
            28 RETURN F5 -> None
        29 F4: left_result = None
        30 F4: right_result = CALL F8(root=4, p=6, q=4)
            31 F8: root is None -> False
            32 F8: root is p or root is q -> True
            33 RETURN F8 -> node(4)
        34 F4: right_result = node(4)
        35 F4: left_result is not None and right_result is not None -> False
        36 F4: left_result is not None -> False
        37 RETURN F4 -> node(4)
    38 F2: right_result = node(4)
    39 F2: left_result is not None and right_result is not None -> True
    40 RETURN F2 -> node(5)
41 F1: left_result = node(5)
42 F1: right_result = CALL F9(root=1, p=6, q=4)
    43 F9: root is None -> False
    44 F9: root is p or root is q -> False
    45 F9: left_result = CALL F10(root=0, p=6, q=4)
        46 F10: root is None -> False
        47 F10: root is p or root is q -> False
        48 F10: left_result = CALL F11(root=None, p=6, q=4)
            49 F11: root is None -> True
            50 RETURN F11 -> None
        51 F10: left_result = None
        52 F10: right_result = CALL F12(root=None, p=6, q=4)
            53 F12: root is None -> True
            54 RETURN F12 -> None
        55 F10: right_result = None
        56 F10: left_result is not None and right_result is not None -> False
        57 F10: left_result is not None -> False
        58 RETURN F10 -> None
    59 F9: left_result = None
    60 F9: right_result = CALL F13(root=8, p=6, q=4)
        61 F13: root is None -> False
        62 F13: root is p or root is q -> False
        63 F13: left_result = CALL F14(root=None, p=6, q=4)
            64 F14: root is None -> True
            65 RETURN F14 -> None
        66 F13: left_result = None
        67 F13: right_result = CALL F15(root=None, p=6, q=4)
            68 F15: root is None -> True
            69 RETURN F15 -> None
        70 F13: right_result = None
        71 F13: left_result is not None and right_result is not None -> False
        72 F13: left_result is not None -> False
        73 RETURN F13 -> None
    74 F9: right_result = None
    75 F9: left_result is not None and right_result is not None -> False
    76 F9: left_result is not None -> False
    77 RETURN F9 -> None
78 F1: right_result = None
79 F1: left_result is not None and right_result is not None -> False
80 F1: left_result is not None -> True
81 RETURN F1 -> node(5)
82 ans = node(5)
```

## 例子二

```text
          3
        /   \
       5     1
      / \   / \
     2   6 0   8
        / \
       7   4

p = node(6)
q = node(4)
```

```python
p = nodes[6]
q = nodes[4]
ans = Solution().lowestCommonAncestor(root, p, q)
```

```text
01 CALL F1(root=3, p=6, q=4)
02 F1: root is None -> False
03 F1: root is p or root is q -> False
04 F1: left_result = CALL F2(root=5, p=6, q=4)
    05 F2: root is None -> False
    06 F2: root is p or root is q -> False
    07 F2: left_result = CALL F3(root=2, p=6, q=4)
        08 F3: root is None -> False
        09 F3: root is p or root is q -> False
        10 F3: left_result = CALL F4(root=None, p=6, q=4)
            11 F4: root is None -> True
            12 RETURN F4 -> None
        13 F3: left_result = None
        14 F3: right_result = CALL F5(root=None, p=6, q=4)
            15 F5: root is None -> True
            16 RETURN F5 -> None
        17 F3: right_result = None
        18 F3: left_result is not None and right_result is not None -> False
        19 F3: left_result is not None -> False
        20 RETURN F3 -> None
    21 F2: left_result = None
    22 F2: right_result = CALL F6(root=6, p=6, q=4)
        23 F6: root is None -> False
        24 F6: root is p or root is q -> True
        25 RETURN F6 -> node(6)
    26 F2: right_result = node(6)
    27 F2: left_result is not None and right_result is not None -> False
    28 F2: left_result is not None -> False
    29 RETURN F2 -> node(6)
30 F1: left_result = node(6)
31 F1: right_result = CALL F7(root=1, p=6, q=4)
    32 F7: root is None -> False
    33 F7: root is p or root is q -> False
    34 F7: left_result = CALL F8(root=0, p=6, q=4)
        35 F8: root is None -> False
        36 F8: root is p or root is q -> False
        37 F8: left_result = CALL F9(root=None, p=6, q=4)
            38 F9: root is None -> True
            39 RETURN F9 -> None
        40 F8: left_result = None
        41 F8: right_result = CALL F10(root=None, p=6, q=4)
            42 F10: root is None -> True
            43 RETURN F10 -> None
        44 F8: right_result = None
        45 F8: left_result is not None and right_result is not None -> False
        46 F8: left_result is not None -> False
        47 RETURN F8 -> None
    48 F7: left_result = None
    49 F7: right_result = CALL F11(root=8, p=6, q=4)
        50 F11: root is None -> False
        51 F11: root is p or root is q -> False
        52 F11: left_result = CALL F12(root=None, p=6, q=4)
            53 F12: root is None -> True
            54 RETURN F12 -> None
        55 F11: left_result = None
        56 F11: right_result = CALL F13(root=None, p=6, q=4)
            57 F13: root is None -> True
            58 RETURN F13 -> None
        59 F11: right_result = None
        60 F11: left_result is not None and right_result is not None -> False
        61 F11: left_result is not None -> False
        62 RETURN F11 -> None
    63 F7: right_result = None
    64 F7: left_result is not None and right_result is not None -> False
    65 F7: left_result is not None -> False
    66 RETURN F7 -> None
67 F1: right_result = None
68 F1: left_result is not None and right_result is not None -> False
69 F1: left_result is not None -> True
70 RETURN F1 -> node(6)
71 ans = node(6)
```
