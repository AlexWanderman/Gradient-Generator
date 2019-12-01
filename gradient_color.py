# st        sp
# dc6f6f -> ffb5b5
# 012345

st = input('Введите hex значение начала градиента: ')
sp = input('Введите hex значение конца градиента: ')
n = int(input('Введите число промежуточных шагов: ')) + 1

r1, g1, b1 = int(st[0:2], 16), int(st[2:4], 16), int(st[4:6], 16)
r2, g2, b2 = int(sp[0:2], 16), int(sp[2:4], 16), int(sp[4:6], 16)

print(f'\n{r1} {g1} {b1} -> {r2} {g2} {b2}')

rs = (r2 - r1) / n + (1 if r2 - r1 < 0 else 0)
gs = (g2 - g1) / n + (1 if g2 - g1 < 0 else 0)
bs = (b2 - b1) / n + (1 if b2 - b1 < 0 else 0)

print(f'{rs:.3f} {gs:.3f} {bs:.3f}\n')

print(f'1) {st} ({r1} : {g1} : {b1})')
for i in range(n):
    rt = int(r1 + rs * (i + 1))
    gt = int(g1 + gs * (i + 1))
    bt = int(b1 + bs * (i + 1))

    assert 0 <= rt <= 255
    assert 0 <= gt <= 255
    assert 0 <= bt <= 255

    r = hex(rt)[2:].rjust(2, "0")
    g = hex(gt)[2:].rjust(2, "0")
    b = hex(bt)[2:].rjust(2, "0")

    print(f'{i+2}) {r}{g}{b} ({rt} : {gt} : {bt})')
