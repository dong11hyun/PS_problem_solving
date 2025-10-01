def solution(wallpaper):
    rows = []
    cols = []
    for r_indx, row in enumerate(wallpaper):
        if '#' in row:
            for c_indx, char in enumerate(row):
                if char == '#':
                    cols.append(c_indx)
                    rows.append(r_indx)
                
    lux, luy = min(rows), min(cols)
    rdx, rdy = max(rows) + 1, max(cols) + 1
    answer = [lux, luy, rdx, rdy]
    print(answer)

    return answer