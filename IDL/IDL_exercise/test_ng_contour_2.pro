PRO test_ng_contour_2

fig_sav = 0

data = HANNING(600, 600)*100
win = WINDOW(DIMENSIONS=[600, 600], /NO_TOOLBAR)
cn = CONTOUR(data, C_VALUE=[20, 40, 60, 80], C_LABEL_SHOW=1, $
  RGB_TABLE=34, LABEL_COLOR='black', C_THICK=2, $
  FONT_SIZE=12, MARGIN=0.1, /CURRENT)

;cn.FILL = 1

;cno = CONTOUR(data, C_VALUE=[20, 40, 60, 80], C_LABEL_SHOW=1, $
;  COLOR='black', LABEL_COLOR='black', C_THICK=2, /OVERPLOT)
;cno.FONT_SIZE=12

;cn.PLANAR = 0
;cno.ZVALUE = 100

IF fig_sav THEN win.Save, 'figures/ng_contour_2.png', WIDTH=600

END