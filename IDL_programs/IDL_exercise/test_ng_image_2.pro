PRO test_ng_image_2

fig_sav = 0

data1 = HANNING(400, 400)*35
data2 = HANNING(400, 400)*60+30
data3 = HANNING(400, 400)*70+100
PRINT, MIN(data2), MAX(data2)
sz = SIZE(data1, /DIM)

win1 = WINDOW(DIMENSIONS=[sz[0]*3, sz[1]], /NO_TOOLBAR)
im1a = IMAGE(data1, RGB_TABLE=3, MARGIN=0, LAYOUT=[3, 1, 1], /CURRENT)
im1b = IMAGE(data2, RGB_TABLE=3, MARGIN=0, LAYOUT=[3, 1, 2], /CURRENT)
im1c = IMAGE(data3, RGB_TABLE=3, MARGIN=0, LAYOUT=[3, 1, 3], /CURRENT)
IF fig_sav THEN win1.Save, 'figures/ng_image_2A.png', HEIGHT=sz[1]

win2 = WINDOW(DIMENSIONS=[sz[0]*3, sz[1]], /NO_TOOLBAR)
im2a = IMAGE(BYTE(data1), RGB_TABLE=3, MARGIN=0, LAYOUT=[3, 1, 1], /CURRENT)
im2b = IMAGE(BYTE(data2), RGB_TABLE=3, MARGIN=0, LAYOUT=[3, 1, 2], /CURRENT)
im2c = IMAGE(BYTE(data3), RGB_TABLE=3, MARGIN=0, LAYOUT=[3, 1, 3], /CURRENT)
IF fig_sav THEN win2.Save, 'figures/ng_image_2B.png', HEIGHT=sz[1]

END