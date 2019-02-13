field = []
for y in range(61):
    field.append([])
    for x in range(104):
        field[-1].append(0)

for i in range(35, 41):
    for j in range(47, 53):
        field[i][j] = 1

field[39][46], field[39][45], field[39][44] = 1, 1, 1

for i in range(28, 39):
    field[i][44] = 1

for i in range(27, 35):
    field[i][52] = 1

field[27][51], field[27][50] = 1, 1
field[27][44], field[27][45], field[27][46] = 1, 1, 1

field[29][51], field[28][51] = 1, 1
field[28][50], field[28][46] = 1, 1

for i in range(27, 31):
    field[i][49] = 1
    field[i][47] = 1

field[28][45] = 1

for i in range(53, 61):
    field[33][i] = 1

for i in range(28, 33):
    field[i][60] = 1

field[28][59] = 1

for i in range(0, 23):
    field[60][i] = 1
    field[59][i] = 1

for i in range(48, 59):
    field[i][21] = 1
    field[i][22] = 1

for i in range(54, 59):
    for j in range(16, 21):
        field[i][j] = 1

for i in range(14):
    field[58][i] = 1
    field[57][i] = 1

for i in range(16, 21):
    field[48][i] = 1
    field[49][i] = 1

field[47][16] = 1

for i in range(49, 57):
    field[i][0] = 1
    field[i][1] = 1
    field[i][2] = 1

for i in range(44, 47):
    field[40][i] = 1