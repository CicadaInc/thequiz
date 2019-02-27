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
field[50][12] = 1

for i in range(26, 31):
    field[53][i] = 1

# ABC
field[16][58] = 1
field[16][57] = 1
field[17][58] = 1
field[18][58] = 1
field[19][58] = 1
field[20][58] = 1
field[18][59] = 1
field[19][59] = 1
field[18][57] = 1
field[19][57] = 1


for i in range(22, 27):
    for j in range(71, 75):
        field[i][j] = 1

for i in range(16, 21):
    for j in range(57, 60):
        field[i][j] = 1

for i in range(5, 10):
    for j in range(54, 58):
        field[i][j] = 1

for i in range(3, 8):
    for j in range(33, 36):
        field[i][j] = 1

for i in range(6, 11):
    for j in range(10, 14):
        field[i][j] = 1

field[11][11] = 0

for i in range(17, 22):
    for j in range(5, 9):
        field[i][j] = 1

for i in range(30, 35):
    for j in range(4, 8):
        field[i][j] = 1

field[48][11] = 1

for i in range(5):
    field[46][i] = 1

field[45][0] = 1
field[44][0] = 1
field[45][1] = 1

for i in range(55, 62):
    field[34][i] = 1
    field[33][i] = 1

for i in range(29, 34):
    field[i][61] = 1

field[29][60] = 1

# for i in range(76, 80):
# #     for j in range(30, 34):
# #         field[i][j] = 1

for i in range(65, 69):
    for j in range(36, 41):
        field[j][i] = 1

for i in range(41, 46):
    for j in range(60, 64):
        field[i][j] = 1

for i in range(50, 55):
    for j in range(51, 55):
        field[i][j] = 1

for i in range(54, 58):
    for j in range(60, 64):
        field[i][j] = 1

for i in range(38, 43):
    for j in range(80, 84):
        field[i][j] = 1

for i in range(38, 43):
    for j in range(72, 76):
        field[i][j] = 1

for i in range(29, 34):
    for j in range(76, 80):
        field[i][j] = 1

for i in range(46, 53):
    for j in range(65, 76):
        field[i][j] = 1

field[47][64] = 1
field[47][75] = 1
field[48][75] = 1
field[48][64] = 1
field[48][76] = 1
field[47][76] = 1
field[46][76] = 1

for i in range(53, 60):
    for j in range(66, 101):
        field[i][j] = 1

for i in range(45, 50):
    for j in range(92, 98):
        field[i][j] = 1

for i in range(6, 53):
    for j in range(98, 101):
        field[i][j] = 1

for i in range(5, 13):
    for j in range(94, 98):
        field[i][j] = 1

for i in range(22, 27):
    for j in range(91, 95):
        field[i][j] = 1

for i in range(11, 16):
    for j in range(85, 89):
        field[i][j] = 1

for i in range(8, 13):
    for j in range(89, 93):
        field[i][j] = 1

for i in range(7, 12):
    for j in range(79, 83):
        field[i][j] = 1

for i in range(50, 53):
    for j in range(84, 88):
        field[i][j] = 1

for i in range(45, 49):
    for j in range(85, 88):
        field[i][j] = 1

for i in range(3, 10):
    for j in range(70, 74):
        field[i][j] = 1

for i in range(69, 74):
    field[6][i] = 0

for i in range(24):
    for j in range(92 - i, 97 - i):
        if i < 10:
            field[34 - i][j] = 1
            field[35 - i][j] = 1
        else:
            field[33 - i][j] = 1
            field[34 - i][j] = 1

field[10][74] = 1

for i in range(11):
    for j in range(85 + i, 88 + i):
        field[44 - i][j] = 1
        field[45 - i][j] = 1
        field[46 - i][j] = 1

field[42][86] = 1
field[43][85] = 1
field[37][97] = 1
field[38][97] = 1
field[38][96] = 1
field[39][95] = 1
field[40][94] = 1
field[41][93] = 1
field[42][92] = 1
