PRO test_ng_colortable_2

fig_sav = 0

cls = ['yellow', 'green', 'blue', 'red']
ncls = N_ELEMENTS(cls)
ctb = COLORTABLE(cls, NCOLORS=ncls, /TRANSPOSE)
HELP, ctb

data = HANNING(400, 400)
PRINT, MIN(data), MAX(data)
win = WINDOW(DIMENSIONS=[400, 500], /NO_TOOLBAR)
im = IMAGE(BYTSCL(data, TOP=ncls-1), POSITION=[0, 0.2, 1, 1], RGB_TABLE=ctb, /CURRENT)
;cn = CONTOUR(data, N_LEVELS=n, C_VALUE=[0.25, 0.5, 0.75, 1], C_THICK=3, $
;  C_LABEL_SHOW=1, COLOR='black', FONT_STYLE='bold', FONT_SIZE=16, /OVERPLOT)
cb = COLORBAR(TARGET=ctb, RANGE=[MIN(data), MAX(data)], TICKINTERVAL=0.25)

IF fig_sav THEN win.Save, 'figures/ng_colortable_2a.png', WIDTH=400

END