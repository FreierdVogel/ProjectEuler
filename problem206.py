from math import sqrt
for _1 in range(10):
    for _2 in range(10):
        for _3 in range(10):
            for _4 in range(10):
                for _5 in range(10):
                    for _6 in range(10):
                        for _7 in range(10):
                            for _8 in range(10):
                                for _9 in range(10):
                                    a = sqrt(int("1%d2%d3%d4%d5%d6%d7%d8%d9%d0" %(_1, _2, _3, _4, _5, _6, _7, _8, _9)))
                                    if a==int(a):
                                        print(a)
                                        break