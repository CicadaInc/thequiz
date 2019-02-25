field = [[0 for _ in range(102)] for _ in range(60)]

for i in range(36, 41):
    field[i][38] = 1

for i in range(37, 41):
    field[i][37] = 1

for i in range(37, 40):
    field[i][36] = 1

for i in range(37, 41):
    field[i][39] = 1

for i in range(28, 41):
    field[i][45] = 1
    field[i][46] = 1

for i in range(46, 54):
    field[40][i] = 1

for i in range(35, 40):
    field[i][48] = 1

for i in range(48, 53):
    field[35][i] = 1

for i in range(28, 34):
    field[i][47] = 1
    field[i][48] = 1

for i in range(28, 40):
    field[i][53] = 1

for i in range(51, 54):
    field[i][28] = 1
    field[i][27] = 1

for i in range(28, 41):
    field[i][54] = 1

field[28][51], field[28][52] = 1, 1
field[29][51], field[29][52] = 1, 1
field[30][52] = 1
field[31][50], field[30][50] = 1, 1

for i in range(18, 28):
    field[i][48] = 1
    field[i][47] = 1

field[29][50], field[28][50] = 1, 1

field[16][47], field[15][46] = 1, 1
field[17][48] = 1

for i in range(11, 51):
    field[11][i] = 1
    field[12][i] = 1

for i in range(17, 47):
    field[15][i] = 1
    field[14][i] = 1

for i in range(13, 50):
    field[i][12] = 1

for i in range(16, 19):
    field[i][17] = 1

field[16][16] = 1
field[17][16] = 1
field[18][15] = 1
field[19][15] = 1

for i in range(20, 41):
    field[i][15] = 1

for i in range(38, 42):
    field[i][16] = 1

for i in range(40, 43):
    field[i][17] = 1
    field[i][18] = 1

for i in range(41, 45):
    field[i][19] = 1

for i in range(42, 45):
    field[i][20] = 1

field[43][18] = 1

for i in range(21, 34):
    field[44][i] = 1
    field[45][i] = 1

field[46][33] = 1

for i in range(50, 53):
    field[i][33] = 1
field[51][34] = 1

field[50][34] = 1

for i in range(14, 31):
    field[47][i] = 1

field[45][20] = 1

for i in range(48, 53):
    field[i][30] = 1
    field[i][31] = 1

field[52][29] = 1
field[52][26], field[52][25] = 1, 1
field[47][31] = 1
field[53][28] = 0
field[54][26] = 0

for i in range(53, 60):
    field[i][25] = 1

for i in range(34, 43):
    field[52][i] = 1
    field[53][i] = 1

for i in range(53, 60):
    field[i][41] = 1
    field[i][42] = 1

field[55][40], field[56][40] = 1, 1
field[55][39], field[56][39] = 1, 1

for i in range(34, 39):
    field[55][i] = 1
    field[56][i] = 1

for i in range(26, 32):
    field[55][i] = 1
    field[56][i] = 1

field[48][14] = 1
field[49][14] = 1

for i in range(21, 28):
    field[i][51] = 1
for i in range(13, 18):
    field[i][50] = 1

for i in range(15, 25):
    field[50][i] = 1

for i in range(50, 55):
    field[i][21] = 1

for i in range(16, 22):
    field[55][i] = 1

field[56][16] = 1
field[57][16] = 1

for i in range(16):
    field[58][i] = 1

field[52][10] = 1
field[51][9] = 1
field[52][9] = 1
field[51][10] = 1

for i in range(3, 11):
    for j in range(47, 53):
        field[j][i] = 1

field[53][8], field[53][7], field[53][6] = 1, 1, 1
field[49][11] = 1

field[50][2] = 1
field[50][1] = 1
field[50][0] = 1

field[50][11] = 1

for i in range(38, 43):
    for j in range(21, 25):
        field[i][j] = 1

for i in range(23, 28):
    for j in range(18, 21):
        field[i][j] = 1

for i in range(23, 28):
    for j in range(35, 39):
        field[i][j] = 1

for j in range(29, 33):
    for i in range(28, 33):
        field[i][j] = 1

field[18][46] = 1
field[16][45] = 1
field[17][46] = 1
