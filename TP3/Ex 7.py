a = 0
while a < 9:
    a += 1
    b = 0
    while b < 9:
        b += 1
        if b == a:
            continue
        c = 0
        while c < 9:
            c += 1
            if c == b or c == a:
                continue
            d = 0
            while d < 9:
                d += 1
                if d == c or d == b or d == a:
                    continue
                e = 0
                while e < 9:
                    e += 1
                    if e == d or e == c or e == b or e == a:
                        continue
                    f = 0
                    while f < 9:
                        f += 1
                        if f == e or f == d or f == c or f == b or f == a:
                            continue
                        g = 0
                        while g < 9:
                            g += 1
                            if g == f or g == e or g == d or g == c or g == b or g == a:
                                continue
                            h = 0
                            while h < 9:
                                h += 1
                                if h == g or h == f or h == e or h == d or h == c or h == b or h == a:
                                    continue
                                i = 0
                                while i < 9:
                                    i += 1
                                    if i == h or i == g or i == f or i == e or i == d or i == c or i == b or i == a:
                                        continue
                                    if (((((((((((a + 13) * b) / c) + d) + 12) * e) - f) - 11) + g) * h) / i) - 10 == 66:
                                        print(a, b, c, d, e, f, g, h, i)
