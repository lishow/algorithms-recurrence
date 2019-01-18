"""
解决百钱百鸡问题
一只公鸡5元、一只母鸡3元、三只小鸡1元
100元100只鸡，多少公鸡多少母鸡多少小鸡
"""
for gj in range(0,20):
    for mj in range(0,33):
        xj = 100 - gj - mj
        if xj/3 + mj*3 + gj*5 == 100:
            print("公鸡有 %d 只，母鸡有 %d 只，小鸡有 %d 只" % (gj, mj, xj))
