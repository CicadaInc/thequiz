field = []
for y in range(61):
    field.append([])
    for x in range(104):
        field[-1].append(0)

for j in range(35, 41):
    for i in range(48, 54):
        field[j][i] = 1

for i in range(27, 35):
    field[i][53] = 1

field[29][52], field[28][52] = 1, 1
field[40][47], field[40][46], field[40][45] = 1, 1, 1

for i in range(27, 40):
    field[i][44] = 1

for i in range(27, 31):
    field[i][50] = 1
    field[i][48] = 1

field[27][46], field[27][51] = 1, 1
field[27][47] = 1
field[27][45] = 1
field[27][52] = 1