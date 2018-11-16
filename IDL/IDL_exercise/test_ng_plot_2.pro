PRO test_ng_plot_2

fig_sav = 0

win = WINDOW(DIMENSIONS=[600, 500], /NO_TOOLBAR)
x = FINDGEN(37)*10
y = SIN(x*!DTOR)
pl = PLOT(x, y, XRANGE=[0, 360], XMAJOR=5, THICK=2, $
  SYMBOL='circle', /SYM_FILLED, SYM_FILL_COLOR='crimson', $
  SYM_SIZE=1.5, XTITLE='Degree', YTITLE='Value', CLIP=0, /CURRENT)

IF fig_sav THEN win.Save, 'figures/ng_plot_2A.png', WIDTH=600

pl.Linestyle = 6
tx1 = TEXT(270, 0.5, 'Positive', COLOR='green', FONT_SIZE=16, $
  ALIGNMENT=0.5, /DATA)
tx2 = TEXT(90, -0.5, 'Negative', COLOR='red', FONT_SIZE=16, $
  ALIGNMENT=0.5, /DATA)

IF fig_sav THEN win.Save, 'figures/ng_plot_2.png', WIDTH=600

END