PRO test_ng_colortable_1

fig_sav = 0

ctb = COLORTABLE(['yellow', 'blue'])
;ctb = COLORTABLE([[255, 255, 0], [0, 0, 255]])
;ctb = COLORTABLE(['yellow', 'lime', 'blue', 'red'])
;ctb = COLORTABLE(['yellow', 'lime', 'violet', 'magenta'])
;ctb = COLORTABLE(['gold', 'green', 'navy', 'crimson'])
HELP, ctb

data = HANNING(400, 400)
win = WINDOW(DIMENSIONS=[400, 500], /NO_TOOLBAR)
im = IMAGE(data, RGB_TABLE=ctb, POSITION=[0, 0.2, 1, 1], /CURRENT)
cbar = COLORBAR(TARGET=im)

;DEVICE, DECOMPOSED=0
;WINDOW, XSIZE=400, YSIZE=400
;TVLCT, ctb
;TVSCL, data

END