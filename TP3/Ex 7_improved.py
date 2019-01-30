count = 0
for a in range(1, 10):
    for b in range(1, 10):
        if b == a:
            continue
        for c in range(1, 10):
            if c == b or c == a:
                continue
            for d in range(1, 10):
                if d == c or d == b or d == a:
                    continue
                for e in range(1, 10):
                    if e == d or e == c or e == b or e == a:
                        continue
                    for f in range(1, 10):
                        if f == e or f == d or f == c or f == b or f == a:
                            continue
                        for g in range(1, 10):
                            if g == f or g == e or g == d or g == c or g == b or g == a:
                                continue
                            for h in range(1, 10):
                                if h == g or h == f or h == e or h == d or h == c or h == b or h == a:
                                    continue
                                for i in range(1, 10):
                                    if i == h or i == g or i == f or i == e or i == d or i == c or i == b or i == a:
                                        continue
                                    if (((((((((((a + 13) * b) / c) + d) + 12) * e) - f) - 11) + g) * h) / i) - 10 == 66:
                                        count += 1
                                        print(a, b, c, d, e, f, g, h, i)

print(count)
