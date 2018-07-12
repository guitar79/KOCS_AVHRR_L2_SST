PRO test_ng_image_1

fig_sav = 0

data = HANNING(600, 600)*100
win = WINDOW(DIMENSIONS=[600, 600], /NO_TOOLBAR)
im = IMAGE(data, MARGIN=0, /CURRENT)

;im.RGB_TABLE = 3

IF fig_sav THEN win.Save, 'figures/ng_image_1.png', WIDTH=600

END