PRO test_ng_plot_multi

fig_sav = 0

x = FINDGEN(37)*10
y1 = SIN(x*!DTOR)
y2 = COS(x*!DTOR)
win = WINDOW(DIMENSIONS=[1000, 400], /NO_TOOLBAR)

p1 = PLOT(x, y1, SYMBOL='circle', /SYM_FILLED, XRANGE=[0, 360], $
  XTICKINTERVAL=90, XTITLE='Angle', YTITLE='Value', $
  TITLE='Sine Curve', /CURRENT, LAYOUT=[2, 1, 1])
pline1 = POLYLINE([0, 360], [0, 0], LINESTYLE=2, COLOR='green', $
  THICK=2, /DATA)

p2 = PLOT(x, y2, SYMBOL='circle', /SYM_FILLED, XRANGE=[0, 360], $
  XTICKINTERVAL=90, XTITLE='Angle', YTITLE='Value', $
  TITLE='Cosine Curve', /CURRENT, LAYOUT=[2, 1, 2])
pline2 = POLYLINE([0, 360], [0, 0], LINESTYLE=2, COLOR='green', $
  THICK=2, /DATA, TARGET=p2)

IF fig_sav THEN win.Save, 'figures/ng_plot_multi.png', WIDTH=1000

END