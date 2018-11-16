PRO test_ng_coord_system

win = WINDOW(DIMENSIONS=[600, 500], /NO_TOOLBAR)
x = FINDGEN(11)
y = x^2
pl = PLOT(x, y, /CURRENT)
tx1 = TEXT(4, 80, 'Data Coord (4, 80)', COLOR='crimson', FONT_SIZE=12, /DATA)
tx2 = TEXT(0.5, 0.5, 'Normal Coord (0.5, 0.5)', COLOR='green', FONT_SIZE=12, /NORMAL)
tx3 = TEXT(200, 100, 'Device Coord (200, 100)', COLOR='blue', FONT_SIZE=12, /DEVICE)

END