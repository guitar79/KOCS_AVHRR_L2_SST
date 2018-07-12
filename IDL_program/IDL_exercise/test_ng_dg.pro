PRO test_ng_dg

x = FINDGEN(101)
y = SQRT(x)

; Plot in DG
DEVICE, DECOMPOSED=0
WINDOW, XSIZE=600, YSIZE=500, RETAIN=2
PLOT, x, y, COLOR=0, BACKGROUND=255, THICK=2, CHARSIZE=1.5, $
  XTITLE='X Values', YTITLE='Y Values', TITLE='My Plot in DG'
;cap = TVRD(/TRUE)
;WRITE_PNG, 'figures/plot_dg.png', cap

; Plot in NG
win = WINDOW(DIMENSIONS=[600, 500], /NO_TOOLBAR)
p = PLOT(x, y, THICK=2, FONT_SIZE=12, TITLE='My Plot in NG', $
  XTITLE='X Values', YTITLE='Y Values', /CURRENT)
;win.Save, 'figures/plot_ng.png', WIDTH=600

END