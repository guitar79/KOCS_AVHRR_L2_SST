PRO test_ng_contour_3

fig_sav = 0

data = HANNING(600, 600)*100
win = WINDOW(DIMENSIONS=[600, 600], /NO_TOOLBAR)

im = IMAGE(data, RGB_TABLE=34, MARGIN=0.1, /CURRENT)
cn = CONTOUR(data, C_VALUE=[20, 40, 60, 80], C_LABEL_SHOW=1, $
  COLOR='black', LABEL_COLOR='black', C_THICK=2, /OVERPLOT)
cn.FONT_SIZE = 12

;cn = CONTOUR(data, C_VALUE=[20, 40, 60, 80], C_LABEL_SHOW=1, $
;  COLOR='black', LABEL_COLOR='black', C_THICK=2, FONT_SIZE=12, $
;  MARGIN=0.1, /CURRENT)
;im = IMAGE(data, RGB_TABLE=34, /OVERPLOT)
;im.ORDER, /SEND_BACKWARD

IF fig_sav THEN win.Save, 'figures/ng_contour_3.png', WIDTH=600

END