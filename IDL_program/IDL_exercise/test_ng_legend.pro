PRO test_ng_legend

fig_sav = 0

x = FINDGEN(37)*10
y1 = SIN(x*!DTOR)
y2 = COS(x*!DTOR)
win = WINDOW(DIMENSIONS=[600, 500], /NO_TOOLBAR)
p1 = PLOT(x, y1, SYMBOL='square', /SYM_FILLED, SYM_FILL_COLOR='blue', $
  NAME=' SINE', XRANGE=[0, 360], XMAJOR=5, MARGIN=[0.1, 0.1, 0.1, 0.2], $
  FONT_SIZE=12, /CURRENT)
p2 = PLOT(x, y2, SYMBOL='diamond', /SYM_FILLED, SYM_FILL_COLOR='red', $
  NAME=' COSINE', FONT_SIZE=12, /OVERPLOT)
lgd = LEGEND(TARGET=[p1, p2], SHADOW=0, /AUTO_TEXT_COLOR, POSITION=[0.9, 0.95])

IF fig_sav THEN win.Save, 'figures/ng_legend.png', WIDTH=600

END