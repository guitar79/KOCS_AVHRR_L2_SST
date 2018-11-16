PRO test_ng_contour_1

fig_sav = 0

data = HANNING(600, 600)*100
win = WINDOW(DIMENSIONS=[600, 600], /NO_TOOLBAR)
cn = CONTOUR(data, COLOR='black', FONT_SIZE=12, MARGIN=0.1, /CURRENT)

;cn.C_VALUE = [20, 40, 60, 80]
;cn.C_LABEL_SHOW = 1

;cn.C_COLOR = ['orange', 'green', 'blue', 'crimson']
;cn.C_THICK = 2
;cn.LABEL_COLOR = 'black'

;cn.PLANAR = 0

IF fig_sav THEN win.Save, 'figures/ng_contour_1.png', WIDTH=600

END