a,b = map(int, input().split())
c,d = map(int, input().split())

ja = (b*c) + (a*d)
mo = (b*d)

def max_gongyak(ja,mo):
    while mo > 0:
        ja,mo = mo, ja%mo
    return ja
print(f"{ja // max_gongyak(ja,mo)} {mo // max_gongyak(ja,mo)}")