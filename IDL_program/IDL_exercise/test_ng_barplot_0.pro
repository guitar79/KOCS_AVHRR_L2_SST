PRO test_ng_barplot_0

fig_sav = 0

x = FINDGEN(31)*10
y = SQRT(x)

win = WINDOW(DIMENSIONS=[800, 600], /NO_TOOLBAR)
pl1 = PLOT(x, y, SYMBOL='circle', /SYM_FILLED, COLOR='crimson', $
  XRANGE=[0, 300], TITLE='PLOT', MARGIN=0.1, FONT_SIZE=12, $
  /CURRENT, LAYOUT=[1, 2, 1])
pl2 = BARPLOT(x, y, XRANGE=[0, 300], FILL_COLOR='crimson', $
  TITLE='BARPLOT', MARGIN=0.1, FONT_SIZE=12, $
  /CURRENT, LAYOUT=[1, 2, 2])

IF fig_sav THEN win.Save, 'figures/ng_barplot_0.png', WIDTH=800

END