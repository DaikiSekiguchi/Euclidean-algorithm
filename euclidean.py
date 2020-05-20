# coding: utf-8

import rhinoscriptsyntax as rs

def euclidean(num1, num2):
    if num2 > num1:
        a = num2
        b = num1
    else:
        a = num1
        b = num2

    # 商と余りを求める
    q, mod = divmod(a, b)

    while True:
        if mod == 0:
            print("Greatest common divisor is {0}".format(b))
            break

        a = b
        b = mod
        q, mod = divmod(a, b)

def drawEuclidean(num1, num2):
    if num2 > num1:
        a = num2
        b = num1
    else:
        a = num1
        b = num2

    # 商と余りを求める
    q, mod = divmod(a, b)

    # 原点
    origin_p = (0, 0, 0)
    count = 0

    while True:
        for i in range(q):
            p1 = origin_p
            p2 = (origin_p[0]+b, origin_p[1], origin_p[2])
            p3 = (origin_p[0]+b, origin_p[1]-b, origin_p[2])
            p4 = (origin_p[0], origin_p[1]-b, origin_p[2])

            # draw rectangle
            rs.AddPolyline([p1, p2, p3, p4, p1])

            # origin pointの更新
            if count % 2 == 0:  # 偶数の場合
                origin_p = p2
            else:               # 奇数の場合
                origin_p = p4

        # 処理終了判定
        if mod == 0:
            print("Greatest common divisor of {0} and {1} is {2}".format(num1, num2, b))
            break

        # update
        a = b
        b = mod
        q, mod = divmod(a, b)
        count += 1

