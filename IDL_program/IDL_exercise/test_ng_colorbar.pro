PRO test_ng_colorbar

fig_sav = 0

data = HANNING(600, 600)*100+100
win = WINDOW(DIMENSIONS=[600, 700])
im = IMAGE(data, MARGIN=0.1, RGB_TABLE=67, /CURRENT)

cb = COLORBAR(TARGET=im)

;cb.POSITION = [0.2, 0.07, 0.8, 0.12]
;cb.TITLE = 'Value'
;cb.FONT_SIZE = 12
;cb.BORDER = 1

END